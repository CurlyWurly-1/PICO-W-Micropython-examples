from machine import Pin, I2C        #importing relevant modules & classes

from time import sleep

import utime
import socket
import network
import bme280                       #importing BME280 library

# Function to load in html page    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
        
    return html



i2c=I2C(1,sda=Pin(6), scl=Pin(7), freq=400000)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("BT-Wifi1","q1!3£4$5%")

# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
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
        # HTTP-Response send
#        response = web_page()
        bme = bme280.BME280(i2c=i2c)    
        response = get_html('windex.html')
        if hbeat == False:
            hbeat = True
            response = response.replace("%%i1", '*' )   
        else:
            hbeat = False
            response = response.replace("%%i1", ' ' )   
        response = response.replace("%%b1", str(bme.values[0]) )
        response = response.replace("%%b2", str(bme.values[1]) )
        response = response.replace("%%b3", str(bme.values[2]) )
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
#        conn.send('HTTP/1.0 200 OKrnContent-type: text/htmlrnrn')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('connection closed') 
