# https://github.com/robert-hh/SH1106
# Remember - The pin numbers are the GP numbers e.g. pin(10) is really GP10
# Remember - Use the I2C1 bus - I2C0 seems to give "EIO" problems
# Remember - If you have "EIO" problems, try disconnecting and reconnecting power to PICO, and then re-execute program


from machine import Pin, I2C
import sh1106
from time import sleep

sda = Pin(10)
scl = Pin(11)

i2c = I2C(1, scl=scl, sda=sda, freq=400000)

print("I2C Address      : "+hex(i2c.scan()[0]).upper())
print("I2C Configuration: "+str(i2c))

oled = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
oled.sleep(False)
oled.flip()

while True:
    oled.fill(0)
    oled.text('SH1106 Display' , 0, 0, 1)
    oled.text('ii2 (SDA/SCL)', 0, 16, 3)
    oled.text('128x64' , 0, 32, 2)
    oled.text('3.3V, size 1.3', 0, 48, 4)
    oled.show()
    sleep(1)

    oled.fill(0)
    oled.pixel(64,32,1)
    oled.show()
    sleep(0.5)

    oled.fill(0)
    oled.hline(0,32,128,1)
    oled.show()
    sleep(0.5)

    oled.fill(0)
    oled.vline(0, 0, 64, 1)
    oled.show()
    sleep(0.5)

    oled.fill(0)
    oled.line(0, 0, 128, 64, 1)
    oled.show()
    sleep(0.5)

    oled.fill(0)
    oled.rect(20, 20, 64, 32, 1)
    oled.show()
    sleep(0.5)

    oled.fill(0)
    oled.fill_rect(20, 20, 64, 32, 1)
    oled.show()
    sleep(0.5)
    
    for x in range(11, 60, 3):
        oled.fill(0)
        oled.fill_rect(x, 40, 5, 5, 1)
        oled.show()
