import machine
from time import sleep

led = machine.Pin("LED", machine.Pin.OUT)

while True:
   led.off()
   sleep(0.5)
   led.on()
   sleep(0.5)
   
