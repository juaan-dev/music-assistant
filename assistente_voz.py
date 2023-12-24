'''
pip install pydub
'''
'''
pip install gtts
'''
from gtts import gTTS
import os
import subprocess
import platform
import time

def falar_comandos(texto):

    # Cria um objeto gTTS
    tts = gTTS(text=texto, lang='pt')

    # Salva o arquivo de áudio
    tts.save("output.mp3")

    os.system("start output.mp3")  # Este comando funciona no Windows