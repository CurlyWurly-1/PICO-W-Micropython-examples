# Please note:
#   When connected, the IP address will be printed (e.g. 192.168.X.YYY)
#   To see the values of the sensor, use a browser and access URL "http://192.168.X.YYY" 

import network
import socket
from secrets import secrets
from time import sleep
from machine import Pin, I2C        #importing relevant modules & classes
import bme280                       #importing BME280 library

# Function to load in html page    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
    return html

# Set up I2C using pins 6 and 7
i2c=I2C(1,sda=Pin(6), scl=Pin(7), freq=400000)

# Load login data from different file for safety reasons
ssid = secrets['ssid']
pw = secrets['pw']

# Access WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,pw)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 80))
server.listen(5)
print('listening on', addr)
hbeat = True
while True:
    try:
        conn, addr = server.accept()
        conn.settimeout(3.0)
        print('client connected from', addr)
        request = conn.recv(1024)
        conn.settimeout(None)

# HTTP-Request receive
        print('Request:', request)              

            
# Retrieve HTML template
        response = get_html('windex.html')

# Get values from sensor. If not connected, use default values [1,2,3]
# and replace the three "placeholders" with the corresponding variable values 
        try:
            bme = bme280.BME280(i2c=i2c)
            vals = bme.values
        except:
            vals =  [1,2,3]
        response = response.replace("%%b1", str(vals[0]) )
        response = response.replace("%%b2", str(vals[1]) )
        response = response.replace("%%b3", str(vals[2]) )

# Toggle Heartbeat indicator 
        if hbeat == False:
            hbeat = True
            response = response.replace("%%i1", '*' )   
        else:
            hbeat = False
            response = response.replace("%%i1", ' ' )

# Send response back
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('connection closed') 
