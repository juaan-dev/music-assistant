'''
pip install spotify
pip install pygame
'''

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pygame
import time
from assistente_voz import falar_comandos

def manipular_texto_musica(texto):
    musica = texto.split(None, 1)
    print(musica)
    return musica[1]

def player_spotify(song):
    print(song)
    musica = manipular_texto_musica(f"{song}")
    
    # Configuração da API do Spotify
    SPOTIPY_CLIENT_ID = '$_SPOTIPY_CLIENT_ID_$'
    SPOTIPY_CLIENT_SECRET = '$_SPOTIPY_CLIENT_SECRET_$'
    SPOTIPY_REDIRECT_URI = '$_SPOTIPY_REDIRECT_URI_$'  # Pode ser qualquer URI válida
    SCOPE = 'user-read-playback-state user-modify-playback-state user-library-read'

    # Configuração do Pygame
    pygame.init()

    # Configuração do Spotipy
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                client_secret=SPOTIPY_CLIENT_SECRET,
                                                redirect_uri=SPOTIPY_REDIRECT_URI,
                                                scope=SCOPE))

    # Obtém o ID do dispositivo ativo
    devices = sp.devices()
    device_id = devices['devices'][0]['id'] if devices['devices'] else None

    if not device_id:
        print("Nenhum dispositivo encontrado. Certifique-se de estar conectado ao Spotify.")
        exit()

    # Função para reproduzir uma música por URI
    def play_track(track_uri):
        sp.start_playback(device_id=device_id, uris=[track_uri])

    # Função para pausar a reprodução
    def pause_track():
        sp.pause_playback(device_id=device_id)

    # Função para retomar a reprodução
    def resume_track():
        sp.start_playback(device_id=device_id)

    # Função para pular para a próxima faixa
    def next_track():
        sp.next_track(device_id=device_id)

    # Função para retroceder para a faixa anterior
    def previous_track():
        sp.previous_track(device_id=device_id)


    # Função para procurar uma música e retornar o URI da primeira correspondência
    def get_track_uri(musica):
        track_info = []
        results = sp.search(q=musica, type='track', limit=1)
        if results['tracks']['items']:
            nome_musica = results['tracks']['items'][0]['name']
            banda = results['tracks']['items'][0]['artists'][0]['name']
            uri = results['tracks']['items'][0]['uri']
            track_info = [nome_musica, banda, uri]
            return track_info
        else:
            return None

    # Exemplo de utilização
    track_uri = get_track_uri(musica)
    print(track_uri)
    falar_comandos(f"Tocando a música {track_uri[0]} de {track_uri[1]} no spotify")
    time.sleep(6)
    # Exemplo de utilização
    play_track(track_uri[2])
    
    
    # time.sleep(5)  # Aguarde um pouco antes de pausar
    # pause_track()
    # time.sleep(2)  # Aguarde antes de retomar
    # resume_track()
    # time.sleep(2)  # Aguarde antes de pular para a próxima faixa
    # next_track()
    # time.sleep(2)  # Aguarde antes de retroceder para a faixa anterior
    # previous_track()
