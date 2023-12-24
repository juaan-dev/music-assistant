'''
pip install speechrecognition
'''

import speech_recognition as sr
from spotify import player_spotify
from assistente_voz import falar_comandos

def reconhecer_comando():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        #falar_comandos("Fale algo...")
        print("Fale algo...")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            audio = recognizer.listen(source)

            try:
                print("Reconhecendo...")
                texto = recognizer.recognize_google(audio, language='pt-BR')
                print(f"Texto reconhecido: {texto}")
                return texto
            except sr.UnknownValueError:
                pass  # Ignorar se não foi possível reconhecer o áudio
            except sr.RequestError as e:
                print(f"Erro na requisição ao Google Speech Recognition service; {e}")

def main():
    while True:
        comando = reconhecer_comando()

        if "tocar" in comando:
            musica = comando.replace("tocar", "").strip()
            player_spotify(musica)
        elif "parar" in comando or "sair" in comando:
            break

if __name__ == "__main__":
    main()
