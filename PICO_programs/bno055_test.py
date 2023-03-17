# bno055_test.py Simple test program for MicroPython bno055 driver
# https://github.com/micropython-IMU/micropython-bno055
# Copyright (c) Peter Hinch 2019
# Released under the MIT licence.
# Remember - The pin numbers are the GP numbers e.g. pin(10) is really GP10
# Remember - Use the I2C1 bus - I2C0 seems to give "EIO" problems
# Remember - If you have "EIO" problems, try disconnecting and reconnecting power to PICO, and then re-execute program

import machine
import time
from bno055 import *
# Tested configurations
# Pyboard hardware I2C
# i2c = machine.I2C(1)

# Pico: hard I2C doesn't work without this patch
# https://github.com/micropython/micropython/issues/8167#issuecomment-1013696765
#i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))  # EIO error almost immediately
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15), freq=400000)  # This works

print("I2C Address      : "+hex(i2c.scan()[0]).upper())
print("I2C Configuration: "+str(i2c))

# All platforms: soft I2C requires timeout >= 1000μs
# i2c = machine.SoftI2C(sda=machine.Pin(16), scl=machine.Pin(17), timeout=1_000)
# ESP8266 soft I2C
# i2c = machine.SoftI2C(scl=machine.Pin(2), sda=machine.Pin(0), timeout=100_000)
# ESP32 hard I2C
# i2c = machine.I2C(1, scl=machine.Pin(21), sda=machine.Pin(23))
imu = BNO055(i2c, address= 0x29)
calibrated = False
while True:
    time.sleep(0.1)
    if not calibrated:
        calibrated = imu.calibrated()
        print('Calibration required: sys {} gyro {} accel {} mag {}'.format(*imu.cal_status()))
#    print('Temperature {}°C'.format(imu.temperature()))
#    print('Mag       x {:5.0f}    y {:5.0f}     z {:5.0f}'.format(*imu.mag()))
#    print('Gyro      x {:5.0f}    y {:5.0f}     z {:5.0f}'.format(*imu.gyro()))
#    print('Accel     x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.accel()))
#    print('Lin acc.  x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.lin_acc()))
#    print('Gravity   x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.gravity()))
    print('Heading     {:4.0f} roll {:4.0f} pitch {:4.0f}'.format(*imu.euler()))
