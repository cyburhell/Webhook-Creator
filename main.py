# This code is completely made for Educational Purposes only. 
# You are responsible for your own actions.
# Iam not responsible for your actions.
# Use this code at your own risk.
# Made by DISCORD : arandomguyin2024 | GITHUB : arandomguyin2024
import requests
from pystyle import Write, Colors
Write.Print("""
 █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀    ▄████▄   ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄   ▒ ▓███▀ ░░██▓ ▒██▒░▒████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░     ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░    ░          ░░   ░    ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░      ░ ░         ░        ░  ░     ░  ░            ░ ░     ░     
                      ░                                     ░                                                           
""",Colors.red,interval=0)
TOKEN = Write.Input("Enter your token : ", Colors.blue_to_red,interval=0)
channel_id = int(Write.Input("Channel ID : ", Colors.blue_to_cyan, interval=0))
webhook_name = Write.Input("Enter the webhook name : ", Colors.blue_to_cyan,interval=0)
numbers = int(Write.Input("How many webhooks do you want to create? : ", Colors.blue_to_cyan, interval=0)) 
url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
name = {
    "name": webhook_name
}
headers={
    "Authorization": TOKEN,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Content-Type":"application/json"
}

for i in range(numbers):
    Write.Print(f"Creating webhook {i+1}...", Colors.blue_to_cyan,interval=0)
    r = requests.post(url, json=name,headers=headers)

if r.status_code == 200:
    response_data = r.json()
    webhook_url = response_data["url"]
    Write.Print(f"Webhook {i+1} created successfully.", Colors.blue_to_cyan,interval=0)
else:
    Write.Print(f"Failed to create webhook. Status code: {r.status_code}", Colors.red,interval=0)
