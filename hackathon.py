# pip install elevenlabs # comando para instalar
#from elevenlabs import generate, play, voices, set_api_key, save, User, Voice, VoiceSettings
from elevenlabs import play, save, Voice, VoiceSettings
from elevenlabs.client import ElevenLabs

chave_eleven = "sk_1931f8a47c5eaf2f7ca211b263cd07f7393c539304e0ff4b"

#set_api_key(chave_eleven)
client = ElevenLabs(
  api_key=chave_eleven  # Defaults to ELEVEN_API_KEY
)

# Pausas entre frases: <break time="0.5s" />
# Pausas entre palavras: - ou ...

resumo_do_texto = """
Nós somos o grupo 4. <break time="0.5s" />
O nosso tema é : Produção de documentação com 100% de acessibilidade utilizando IA! <break time="0.5s" />
E a nossa EIAI utilizada foi ELEVEN LABS! <break time="0.5s" />
MUITO OBRIGADO E BOA NOITE
"""

# ESCOLHA DE VOZ
voz_escolhida = "George"

#CONFIGURAR A ESTABILIDADE DA VOZ

# Increasing variability can make speech more expressive with output varying between re-generations. It can also lead to instabilities.
# Increasing stability will make the voice more consistent between re-generations, but it can also make it sounds a bit monotone. On longer text fragments we recommend lowering this value.
stability=0.35


#AUMENTO SIMILAR DAS VOZ, PARA PODER CHEGAR MAIS PERTO DA VOZ HUMANA A QUAL FOI GRAVADA

#Low values are recommended if background artifacts are present in generated speech.
#High enhancement boosts overall voice clarity and target speaker similarity. Very high values can cause artifacts, so adjusting this setting to find the optimal value is encouraged.
similarity_boost=0.3

# ESTILO DA LEITURA

#High values are recommended if the style of the speech should be exaggerated compared to the uploaded audio. Higher values can lead to more instability in the generated speech. Setting this to 0.0 will greatly increase generation speed and is the default setting.
style=0.55


# MELHORAR A SEMELHANÇA DA VOZ HUMANA

# Boost the similarity of the synthesized speech and the voice at the cost of some generation speed.
boost = False

#FUNÇÃO DEFINIDA PARA PARA FALAR E SALVAR O ARQUIVO

falar = True
save_file = True


# ESTRUTURA DE CRIAÇÃO DO USUARIO
#user = user.from_api()
user = client.user.get()
restantes = user.subscription.character_limit - user.subscription.character_count
print("Restantes:", restantes, "Total:", user.subscription.character_limit)
# PRINTAR NA TELA O NUMERO DA CARACTERES UTILIZADO E TOTAL QUE PODE SER UTILIZADO
caracteres_total = len(''.join(resumo_do_texto))
print("Total de caracteres", caracteres_total)

# ESTRUTURA PARA INFORMAR SE ATINGIU O LIMITE DE CARACTERES OU NÃO
if restantes < caracteres_total:
    print("Não vai dar pra printar tudo")
    gerar = False
else:
    print("Creditos suficientes")

# ESTRUTURA PARA PRINTAR AS VOZES QUE ESTÃO DISPONIVEIS
text = []
for t in resumo_do_texto:
    if len(t) > 1:
        text.append(t)
#voices = voices()
voices = client.voices.get_all()
voice = None

#ESTRUTURA CRIADA PARA PODER MOSTRAR O NUMEROS DE VOZES DA BIBLIOTECA ELEVENLABS. E QUAL VOZ FOI ESCOLHIDA
for index, voz in enumerate(voices.voices):
    print("voz", index, voz.name)
    if voz_escolhida in voz.name:
        print("Escolhida", voz.name)
        voice = voz.voice_id

# GERAR O RESUMO DO TEXTO, E FAZER A LEITURA DE ACORDO QUE FOI DEFINIDO PELO USUARIO
audio = client.generate(
    text=resumo_do_texto,
    voice=Voice(voice_id=voice,
                settings=VoiceSettings(stability=stability,
                                       similarity_boost=similarity_boost,
                                       style=style,
                                       use_speaker_boost=boost)),
    model='eleven_multilingual_v2'
)

# ESTRUTURA DE FLUXO CRIADA PARA FAZER A LEITURA, E TRANSFORMAR EM AUDIO. E NA HORA DE SALVAR INFORMAR A DATA E O FORMATO SALVO
if falar:
    print("Falando")
    play(audio)
if save_file:
    import time
    hora = time.strftime("%Y%m%d-%H%M%S")
    filename = "./audio_elevenlabs/" + voz_escolhida + "_" + hora + ".mp3"
    print("salvando", filename)
    save(audio=audio,  # Audio bytes (returned by generate)
         filename=filename  # Filename to save audio to (e.g. "audio.wav")
         )
