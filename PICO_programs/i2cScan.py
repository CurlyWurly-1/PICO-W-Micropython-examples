# Remember - The pin numbers are the GP numbers e.g. pin 14 is really GP14
# Remember - Use the I2C1 bus - I2C0 seems to give "EIO" problems
# Remember - If you have "EIO" problems, try disconnecting and reconnecting power to PICO, and then re-execute program

import machine

### BME280
#sda=machine.Pin(6)   # BME280 (Temp)   - Decimal address:  118  | Hexa address:  0x76
#scl=machine.Pin(7)   # BME280 (Temp)   - Decimal address:  118  | Hexa address:  0x76
#i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)

### OLED
#sda=machine.Pin(10)   # OLED (Display) - Decimal address:  60  | Hexa address:  0x3c
#scl=machine.Pin(11)   # OLED (Display) - Decimal address:  60  | Hexa address:  0x3c
#i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)

### BNO055
sda=machine.Pin(14)   # BNO055 (Gyro)   - Decimal address:  41  | Hexa address:  0x29
scl=machine.Pin(15)   # BNO055 (Gyro)   - Decimal address:  41  | Hexa address:  0x29
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)


print('Scan i2c bus...')
devices = i2c.scan()
 
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
 
  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))

