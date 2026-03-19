#!/bin/bash
# Carga credenciales desde archivo de configuración
CONFIG="$HOME/.config/spotify-nowplaying/config"
if [ ! -f "$CONFIG" ]; then
    echo "Error: no existe $CONFIG"
    exit 1
fi
source "$CONFIG"

# Obtener access token
ACCESS_TOKEN=$(curl -s -X POST "https://accounts.spotify.com/api/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token&refresh_token=$REFRESH_TOKEN&client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET" \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

# Obtener canción actual
RESPONSE=$(curl -s -X GET "https://api.spotify.com/v1/me/player/currently-playing" \
  -H "Authorization: Bearer $ACCESS_TOKEN")

ARTIST=$(echo $RESPONSE | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['item']['artists'][0]['name'])" 2>/dev/null)
TRACK=$(echo $RESPONSE | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['item']['name'])" 2>/dev/null)

if [ -z "$ARTIST" ]; then
    echo "Sin música"
else
    echo "$ARTIST" | fold -s -w 7
    echo "---"
    echo "$TRACK" | fold -s -w 7
fi
