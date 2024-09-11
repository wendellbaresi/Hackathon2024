import pyttsx3 #UTILIZANDO A BIBLIOTECA IMPORT PYTTSX3 É UMA BIBLIOTECA QUE TRABALHA COM VOICES#

speaker = pyttsx3.init() #Iniciando a biblioteca que foi baixada#

texto = "Ola Mundo, estamos participando do HACKATHON 2024, e somos o grupo 4" #Criando a variavel de texto, para fazer a leitura#

Ler = open('Local do arquivo.txt', 'r' , encoding = 'utf8') #Variavel para abrir um arquivo e fazer a leitura, seguindo as normas e caracteres portugues UTF-8

texto = Ler.read() # função para fazer a leitura

voices = speaker.getProperty('voices') #Criando a variavel que vai ser definida como propriedade, que vai salvar as vozes do computador#

for voice in voices: #Definição de vozes do computador, ao executar vai mostrar quais vozes o seu computador tem. Exemplo: Voz em Inglês, Voz em Português ou Voz em Espanhol#
    print(voice, voice.id) #Função para escrever na tela as opções de vozes que tem no computador, para o usuario fazer a escolha#

speaker.setProperty('voice', voices[0].id) #Função que foi definida a voz#

rate = speaker.getProperty('rate') #Variavel para definir velocidade da voz ao executar a leitura do texto#

speaker.setProperty('rate', rate-50) # função rate para definir a velocidade. EX: rate-50 (mais lento); rate+50 (mais rapido)#

print(texto)
speaker.say(texto)
speaker.runAndWait()
