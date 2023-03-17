# PICO-W-Micropython-examples
For the PICO W (RP2040 with WIFI) - A collection of Micropython programs that you can use for the following modules:
 - OLED (size 1.3) - Display that uses the SH1106 driver instead of the SSD1306 driver
 - GPS Module      - GPS co-ordinates
 - BNO0055 module  - 6 axis Gyro
 - BME280 module   - Temp, pressure, Humidity

N.B. Be aware that if you want to connect all four devices to the PICO W at the same time, this means that 4 pairs of 3.3V/Gnd power connections will be required.
Unfortunately, there is only one 3.3V pin on the PICO so unless you use a breadboard to connect things up, you will have to create some sort of power split harness (e.g. 1 pair of wires in with 4 pairs out).

If you don't want to do this, you could use a breadboard, but you might find you need to add 1K pullup resistors to the SDA and SCL lines (to 3.3V). These pullup resistors may be necessary to counteract the effect of capacitance between the breadboard lines which lowers the impedance between pins at high frequency (e.g. when set at 400,000).

In my case, to supply power to each module I constructed a 3.3V/GND harness out of dupoint wires, and used separate pairs of dupoint wires for each module's communication pins.  Whilst I didn't have to add any pull up resistors to the SDA/SCL wires, I did notice that I had to use the I2C1 bus for the modules to work OK.

Also, if you get the "EIO" error, try disconnecting and reconnecting power to the PICOW (i.e. pull out and push back in the USB cable). This fixed the problem for me. The error seems to occur when you press "Ctrl/C" in Thonny to stop a program, and then try to execute another program in Thonny. 

<img src="/images/picow_pinout.png" alt="PICO W Pinout"/>


# Step 1 - Attach OLED and execute "oled_sh1106.py"  
This tests the 1.3 OLED Display that uses a SH1106 driver instead of SSD1306 driver

Attach 1.3 OLED module as follows
 - 3.3V power   -> pin 37 (3v3_en)
 - Grnd         -> pin 38 (Gnd) 
 - SDA          -> pin 14 (GP10)
 - SCL          -> pin 15 (GP11)

# Step 2 - Attach GPS module and execute "gpsDisplay.py" 
This tests both the GPS Module and the OLED

Attach GPS Module as follows
 - 3.3V power   -> pin 37 (3v3_en)
 - Grnd         -> pin 38 (Gnd) 
 - RX           -> pin 11 (GP8)
 - TX           -> pin 12 (GP9)

# Step 3 - Attach BNO0055 and execute "bno055_test.py" 
This tests the BNO055 module and outputs to serial
 - 3.3V power   -> pin 37 (3v3_en)
 - Grnd         -> pin 38 (Gnd) 
 - SDA          -> pin 19 (GP14)
 - SCL          -> pin 20 (GP15)

# Step 4 - Attach BME280 and execute "bme280_test.py" 
This tests the BNO055 module and outputs to serial
 - 3.3V power   -> pin 37 (3v3_en)
 - Grnd         -> pin 38 (Gnd) 
 - SDA          -> pin  9 (GP6)
 - SCL          -> pin 10 (GP7)
