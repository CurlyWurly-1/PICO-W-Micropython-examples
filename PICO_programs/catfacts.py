"""
Get a cat fact from the internet!
You will need to add your wireless SSID and password to secrets.py (and save this file to your Pico in library called "lib")
"""

import network
import requests
from secrets import secrets
from time import sleep

# connect to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(False)
wlan.active(True)
ssid = secrets['ssid']
pw = secrets['pw']
wlan.connect(ssid, pw)
while wlan.isconnected() is False:
    print('Waiting for connection...')
    sleep(1)

request = requests.get('http://catfact.ninja/fact').json()
fact = request['fact']
print('Cat fact!')
print(fact)
