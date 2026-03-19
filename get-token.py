import requests
import urllib.parse
import http.server
import webbrowser

CLIENT_ID = "TU_CLIENT_ID_AQUI"
CLIENT_SECRET = "TU_CLIENT_SECRET_AQUI"
REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPE = "user-read-currently-playing user-read-playback-state"

auth_url = f"https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={urllib.parse.quote(REDIRECT_URI)}&scope={urllib.parse.quote(SCOPE)}"

print("Abre esta URL en el navegador:")
print(auth_url)
code = input("Pega el 'code' de la URL de redirección: ")

response = requests.post("https://accounts.spotify.com/api/token", data={
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": REDIRECT_URI,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
})

tokens = response.json()
print("Respuesta completa:", tokens)
print(f"\nRefresh Token: {tokens['refresh_token']}")
