# Spotify Now Playing - OpenDeck Plugin

Plugin para OpenDeck que muestra el artista y canción actual de Spotify en tu Stream Deck Neo (y otros modelos).

## Requisitos

- [OpenDeck](https://github.com/nekename/OpenDeck)
- Python 3
- `python-websocket-client` (`paru -S python-websocket-client`)
- Cuenta de Spotify Premium
- API de Spotify (Client ID y Client Secret)

## Crear app en Spotify Developer

1. Ve a [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard) e inicia sesión
2. Pulsa **Create app**
3. Rellena el formulario:
   - **App Name**: `Stream Deck` (o el que quieras)
   - **App description**: `Stream Deck plugin integration`
   - **Redirect URI**: `http://127.0.0.1:8888/callback` → pulsa **Add**
   - Marca la casilla **Web API**
4. Acepta los términos y pulsa **Save**
5. En el dashboard de tu app pulsa **Settings**
6. Copia el **Client ID**
7. Pulsa **View client secret** y cópialo también

## Obtener el Refresh Token

1. Copia `get-token.py` a tu carpeta home
2. Edita el archivo y pon tu **Client ID** y **Client Secret**
3. Ejecuta:
```bash
   python3 get-token.py
```
4. Abre la URL en el navegador y autoriza
5. Copia el `code` de la URL de redirección (aunque diga error de conexión)
6. Pégalo en la terminal
7. Copia el **Refresh Token** que aparece

## Instalación

# 1. Clona el repo
```bash
git clone https://github.com/SergioSoria12/spotify-nowplaying-opendeck
cd spotify-nowplaying-opendeck
```

### 2. Copia el plugin a OpenDeck
```bash
cp -r com.sergio.nowplaying.sdPlugin ~/.config/opendeck/plugins/
```

### 3. Copia el script de Spotify
```bash
cp spotify-now-playing.sh ~/.local/bin/
chmod +x ~/.local/bin/spotify-now-playing.sh
```

### 4. Configura tus credenciales de Spotify
```bash
mkdir -p ~/.config/spotify-nowplaying
nano ~/.config/spotify-nowplaying/config
```

Añade:
```bash
CLIENT_ID="tu_client_id"
CLIENT_SECRET="tu_client_secret"
REFRESH_TOKEN="tu_refresh_token"
```

Para obtener el Refresh Token usa el script `get-token.py` incluido.

### 5. Configura el Redirect URI en Spotify Developer Dashboard
Añade `http://127.0.0.1:8888/callback` en tu app de Spotify.

### 6. Reinicia OpenDeck
El plugin aparecerá bajo la categoría **Spotify** en el panel de acciones.

## Configuración del botón en OpenDeck

- Arrastra **Now Playing** al botón deseado
- Clic derecho → Edit:
  - Color del texto: `#1DB954`
  - Tamaño de fuente: `13`
  - Negrita: activada
  - Fondo: negro `#000000`

## Notas

- El texto se refresca automáticamente cada 5 segundos
- Requiere Spotify abierto y reproduciendo música
