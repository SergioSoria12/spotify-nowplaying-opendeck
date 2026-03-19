#!/usr/bin/env python3
import websocket
import json
import time
import subprocess
import threading
import sys

PORT = None
PLUGIN_UUID = None
contexts = []

def get_now_playing():
    result = subprocess.run(
        ["/home/sergio/.local/bin/spotify-now-playing.sh"],
        capture_output=True, text=True
    )
    return result.stdout.strip()

def update_buttons(ws):
    last_text = ""
    while True:
        try:
            text = get_now_playing()
            if text != last_text:
                last_text = text
                for ctx in contexts:
                    msg = {
                        "event": "setTitle",
                        "context": ctx,
                        "payload": {
                            "title": text,
                            "target": 0
                        }
                    }
                    ws.send(json.dumps(msg))
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(5)
              
                  
def on_open(ws):
    reg = {
        "event": "registerPlugin",
        "uuid": PLUGIN_UUID
    }
    ws.send(json.dumps(reg))
    print("Plugin registrado")
    t = threading.Thread(target=update_buttons, args=(ws,), daemon=True)
    t.start()

def on_message(ws, message):
    global contexts
    data = json.loads(message)
    event = data.get("event", "")
    if event in ("willAppear", "keyDown"):
        ctx = data.get("context")
        if ctx and ctx not in contexts:
            contexts.append(ctx)
    elif event == "willDisappear":
        ctx = data.get("context")
        if ctx in contexts:
            contexts.remove(ctx)

def on_error(ws, error):
    print(f"Error WS: {error}")

def on_close(ws, *args):
    print("Desconectado")

# Parsear argumentos de OpenDeck
args = sys.argv[1:]
for i, arg in enumerate(args):
    if arg == "-port":
        PORT = int(args[i+1])
    elif arg == "-pluginUUID":
        PLUGIN_UUID = args[i+1]

if not PORT or not PLUGIN_UUID:
    print("Faltan argumentos -port y -pluginUUID")
    sys.exit(1)

ws = websocket.WebSocketApp(
    f"ws://localhost:{PORT}",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

ws.run_forever()
