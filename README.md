# Music Assistant 🎵🎤

O Music Assistant é um projeto desenvolvido para permitir que os usuários controlem o Spotify através de comandos de voz. Com esta aplicação, os usuários podem solicitar músicas, pausar, reproduzir e controlar diversas funcionalidades do Spotify usando apenas a voz.

## Funcionalidades

- Controle do Spotify por meio de comandos de voz.
- Reprodução de músicas, pausa, avanço e retrocesso.
- Acesso à biblioteca de músicas do usuário no Spotify.

## Configuração da API do Spotify

Primeiramente, você deve ser Premium no Spotify para utilizar o Music Assistant, pois é necessário configurar a API do Spotify com as credenciais de desenvolvedor. Siga as instruções abaixo para configurar as credenciais:

1. Acesse o [Dashboard de Desenvolvedor do Spotify](https://developer.spotify.com/dashboard/).
2. Crie um aplicativo e anote o Client ID e o Client Secret.
3. Defina uma Redirect URI válida (pode ser qualquer URI válida).
4. Preencha as seguintes variáveis no arquivo de configuração do projeto:

```python
# Configuração da API do Spotify
SPOTIPY_CLIENT_ID = '$_SPOTIPY_CLIENT_ID_$'
SPOTIPY_CLIENT_SECRET = '$_SPOTIPY_CLIENT_SECRET_$'
SPOTIPY_REDIRECT_URI = '$_SPOTIPY_REDIRECT_URI_$'  # Pode ser qualquer URI válida
SCOPE = 'user-read-playback-state user-modify-playback-state user-library-read'
```

Substitua `$_SPOTIPY_CLIENT_ID_$`, `$_SPOTIPY_CLIENT_SECRET_$` e `$_SPOTIPY_REDIRECT_URI_$` pelas suas credenciais e URI.

## Instalação

Antes de executar o Music Assistant, é necessário instalar as seguintes dependências do Python:

```bash
pip install spotify
pip install pygame
pip install speechrecognition
pip install gtts
pip install pydub
```

## Execução

Para executar o Music Assistant, digite o seguinte comando no terminal:

```bash
python reconhecimento_voz.py
```

## Execução dos Comandos

Dependendo do comando reconhecido, o assistente de música toma ações específicas:

- **Comando "tocar":** Se o comando contiver a palavra "tocar", o assistente interpreta que o usuário deseja reproduzir uma música no Spotify. Ele extrai o nome da música do comando e chama a função `player_spotify()` para executar a música especificada.
    <br>
    Suponha que você esteja usando o assistente de música e deseje reproduzir a música "Bohemian Rhapsody" do Spotify. Você diria algo como:<br>
        ```
        Tocar Bohemian Rhapsody
        ```
      <br>O assistente reconheceria o comando e extrairia o nome da música, que é "Bohemian Rhapsody". Em seguida, ele chamaria a função `player_spotify()` para iniciar a reprodução dessa música específica no Spotify.

- **Comandos "parar" ou "sair":** Se o comando contiver "parar" ou "sair", o loop principal é encerrado, e o assistente de música finaliza sua execução.



<br><br><br>
Divirta-se! 🎵🎤
