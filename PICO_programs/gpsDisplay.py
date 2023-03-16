# https://github.com/robert-hh/SH1106
from machine import UART, Pin
from machine import Pin, I2C
import sh1106
from time import sleep

sda = Pin(0)
scl = Pin(1)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)
#print("I2C Address      : "+hex(i2c.scan()[0]).upper())
#print("I2C Configuration: "+str(i2c))
oled = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
oled.sleep(False)
oled.flip()

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9), bits=8, parity=None, stop=1)
#uart1.write(b'UART on GPIO8 & GPIO9 at 9600 baud\n\r')

#uart0 = UART(0)
#uart0.write(b'UART on GPIO0 & GPIO1 at 115200 baud\n\r')

oled.text('GPS Display' , 0, 0, 1)
oled.text('Waiting...', 0, 16, 3)

while True:
    rec = False
    rxData = bytes()
    while uart1.any() > 0:
        rec = True
        rxData += uart1.read()
    if rec == True:
        rec = False
#        print(rxData.decode())
        try:
            msgArr = rxData.decode().split("\n")
            try:
                try:
                    for z_rec in msgArr:
                        if z_rec[1:6] == "GNGGA":
                            GNGGA_str = z_rec
                except:
                    GNGGA_str =",,,,"
            except:
                GNGGA_str = ",,,,"

            print(GNGGA_str)
            g1 = " "
            g2 = " "
            g3 = " "
            g4 = " "
            g5 = " "
            try:
                GNGGA_ary = GNGGA_str.split(",")
                g1 = GNGGA_ary[1]
                g2 = GNGGA_ary[2]
                g3 = GNGGA_ary[3]
                g4 = GNGGA_ary[4]
                g5 = GNGGA_ary[5]
            except:
                print("GNGGA error")

            z_time = "*Time?"
            z_lat  = "*lat?"
            z_lng  = "*lng?"
            try:
                if g1 != False:
                    z_chars = str(int(float(g1) + 1000000))  # Pad out the number so that it is easier to slice it 
                    z_time = z_chars[1:3] + ":" + z_chars[3:5] + ":" + z_chars[5:]
                if g2 != False:
#                    x = float(g2[2:])/60
#                    print(x) 
#                    y = round(float(g2[2:])/60,6)
#                    print(y)
                    z_lat = str(round(float(g2[0:2])+(float(g2[2:])/60), 9))
#                    z_lat = str(int(g2[0:2]))+str(round(float(g2[2:])/60),6)[1:]
#                    z_lat = str(int(g2[0:2]))+str(round(float(g2[2:])/60,6))[1:]
                    z_lat = z_lat.strip("0")
                    if g3 != 'N':
                        z_lat = "-"+z_lat
                    res = '    '
                    indx = 0
                    for indx in range(0, 5):
                        res = res[1:]
                        if z_lat[indx] == ".":
                            break
                    z_lat = res + z_lat
                if g4 != False:                     
                    z_lng = str(round(float(g4[0:3])+(float(g4[3:])/60), 9))
#                    z_lng = str(int(g4[0:3]))+str(round(float(g4[3:])/60),6)
#                    z_lng = str(int(g4[0:3]))+str(round(float(g4[3:])/60,6))[1:]
                    z_lng = z_lng.strip("0")
                    if g5 != 'W':
                        z_lng = "-"+ z_lng
                    res = '    '
                    indx = 0
                    for indx in range(0, 5):
                        res = res[1:]
                        if z_lng[indx] == ".":
                            break
                    z_lng = res + z_lng

            except:
                print("calc error")
                
            oled.fill(0)
            oled.text('GPS Display' , 0, 0, 1)
            oled.text(z_time , 0, 16, 2)  # Time
            oled.text(z_lat , 0, 32, 2)  # Latitude
            oled.text(z_lng , 0, 48, 2)  # Longitude
            oled.show()
        except:
            oled.fill(0)
            oled.text('GPS Display' , 0, 0, 1)
            oled.text('Array Error' , 0, 32, 2)
            oled.text('           ' , 0, 48, 2)
