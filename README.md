# PICO-W-Micropython-examples
For the PICO W (RP2040 with WIFI) - A collection of Micropython programs that you can use for the following modules:
 - OLED (size 1.3) - Display that uses the SH1106 driver instead of the SSD1306 driver
 - GPS Module      - GPS co-ordinates
 - BNO0055 module  - 6 axis Gyro
 - BME280 module   - Temp, pressure, Humidity
 - On-board Wifi 

The purpose of this page is to enable you to get started using these modules. Once all is connected and working OK, you could copy the relevant code from the programs to create your own "thing" e.g. display the temperature or compass heading on your own webpage. The main thing is that you can do this knowing that the modules are all connected correctly and working OK.  

N.B. Be aware that if you want to connect all four devices to the PICO W at the same time, then 4 pairs of 3.3V/Gnd power connections will be required.
Unfortunately, there is only one 3.3V pin on the PICO so unless you use a breadboard to connect things up, you will have to create some sort of power split harness (e.g. 1 pair of wires in with 4 pairs out).

If you don't want to do this, you could use a breadboard, but you might find you need to add 1K pullup resistors to the SDA and SCL lines (to 3.3V). These pullup resistors may be necessary to counteract the effect of capacitance between the breadboard lines which lowers the impedance between pins at high frequency (e.g. when set at 400,000).

In my case, to supply power to each module I constructed a 3.3V/GND harness out of dupoint wires, and used separate pairs of dupoint wires for each module's communication pins.  Whilst I didn't have to add any pull up resistors to the SDA/SCL wires, I did notice that I had to use the I2C1 bus for the modules to work OK.
If you wanted to make a permanent installation of the programs/circuits. you really should add a Pullup 1K resistor to both the SDA and SCL line 

# The "EIO" Error
This happens with I2S devices. 

If you get the "EIO" error, try disconnecting and reconnecting power to the PICOW (i.e. pull out and push back in the USB cable) and restarting the backend in Thonny (press the red "Stop/Restart" button in the menu bar). This seemed to temporarily fix the problem for me. The error mostly occurs in the situation when I had pressed "Ctrl/C" in Thonny to stop a program executing, and then tried to load/execute another program, with the error occuring just at the start when executing the new program. Disconnecting and reconnecting power, and pressing the red "stop/Restart" button in Thonny seemed to reset things fine with the "EIO" error no longer happening thereafter. Of course, if you load/execute yet another program which uses a different I2S device, it seems you have to repeat this annoying workaround fix. I guess when you have decided on your final circuit arrangement, this strange effect does not occur.    

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

# Other program 1 - "i2sScan.py"
This scans for any connected I2S modules. You do have to configure it to listen on various pin pairs.

# Other program 2 - "netScan.py"
This sniffs for wifi access points and lists any SSID found (It doesn't need any modules).

# Other program 3 - "uart.py"
This is a general use UART (TX/RX) program. If it receives anything, it prints to serial. You can configure it to listen on various pin pairs and at different BAUD rates

# Other program 4 - "wifi_sta"
This will set up a webserver page where you can control the onboard (green) LED on or off. You first need to modify the code in "secrets.py" with your SSID and SSID password. (It doesn't need any modules). When the program executes, it will try to connect to your wifi. If it connects, the serial window will display the IP address that has been assigned. Go to a web browser and enter this IP adress (it will be something like http://192.168.1.XXX where you have to change the last three digits). This IP address shoudl show a webpage with two buttons. If you press the appropriate button, you can switch the onboard green LED on and off.

N.B. the webpage that you see, is parsed from "index.html". You can adapt "index.html" to show whatever you want, as long as the buttons still work
