# Remember - The pin numbers are the GP numbers e.g. pin 14 is really GP14
# Remember - Use the I2C1 bus - I2C0 seems to give "EIO" problems
# Remember - If you have "EIO" problems, try disconnecting and reconnecting power to PICO, and then re-execute program


from machine import Pin, I2C        #importing relevant modules & classes
from time import sleep
import bme280       #importing BME280 library

i2c=I2C(1,sda=Pin(6), scl=Pin(7), freq=400000)
while True:
  bme = bme280.BME280(i2c=i2c)          #BME280 object created
  print(bme.values)
  sleep(10)           #delay of 10s