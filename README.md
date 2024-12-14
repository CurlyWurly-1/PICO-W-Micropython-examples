# PICO-2-W-Micropython-examples

This is a collection of 11 Micropython programs that you can use for the following modules: 
 - OLED (size 1.3) - Display that uses the SH1106 driver instead of the SSD1306 driver
 - GPS Module      - GPS co-ordinates
 - BNO0055 module  - 6 axis Gyro
 - BME280 module   - Temp, pressure, Humidity
 - On-board Wifi 

## Purpose of this repro and how to use it 
The purpose of this page is to enable you to get started using these modules. Once all is connected and working OK, you could copy the relevant code from the programs to create your own "thing" e.g. Your own webpage that displays values of Temperature/Humidity/GPS Co-ordinates/Compass bearing. The main plus point is that you can do this subsequent adaption, knowing that your modules are already connected up and working OK. 

All you have to do is methodically follow Steps 1 to 4 as outlined in the below section called **"THE PROGRAMS, HOW TO USE AND THEIR SEQUENCE"** .

## Firmware
To get hold of the "PICO 2 W" (RP2350 with wifi) firmware file, look at the appropriate download link on the [Raspberry Pi Pico Micropython page](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython)

_N.B. This webpage has download links for other Pico versions e.g. for the firmware file applicable to a "PICO W" (RP2040 with WiFi)_

## Assumptions
 - This page assumes that you have already set up your PICO W (or PICO 2 W) with the correct firmware, as discussed above.  
 - You have installed "Thonny" (https://thonny.org) in your desktop/laptop, and checked that the PICO W (or PICO 2 W) can communicate OK with "Thonny" software. If this hasn't been done yet, please refer to the PICO W (or (PICO 2 W) setup instructions with Thonny (easy enough to find via g0ggle). Once you have completed the setup, come back here for these programs.  
 - If the OLED still doesn't work, try using the SSD1306 driver https://how2electronics.com/interfacing-ssd1306-oled-display-with-raspberry-pi-pico/)
 
 FROM NOW ON, THE TERM "PICO W" WILL BE USED TO DESCRIBE THE "PICO W" or the "PICO 2 W" 

## How to install the programs in Thonny
 - Download the zip file of this repo and unzip it.
 - In Thonny, press "View" -> "Files" to bring up the copy sidebar and copy all the content from the downloaded directory called "PICO_programs" to your PICO W. Do this until you see the following content in your PICO W memory:
   - The main directory in your PICO W contains 11 Micropython programs, two HTML files (called "index.html" and "windex.html") and a new directory called "lib"
   - The directory "lib" contains 4 Micropython modules and also the "secrets.py" file. (5 objects in total) N.B. Once the "secrets.py" file is manually updated with your particular SSID and password, all the WiFi related programs will work OK in your PICO W.     

## Physical wiring considerations
Be aware that if you don't want to use a breadboard to connect all four devices to the PICO W (at the same time) then 4 pairs of 3.3V/Gnd power connections will be required.
Unfortunately, there is only one 3.3V pin on the PICO so you will have to create some sort of power split harness (e.g. 1 pair of wires in with 4 pairs out).

In my case, to supply power to each module I constructed a 3.3V/GND harness out of dupoint wires, and used separate pairs of dupoint wires for each module's communication pins.  Whilst I didn't have to add any pull up resistors to the SDA/SCL wires, I did notice that I had to use the I2C1 bus for the modules to work OK (instead of the I2C0 bus).

If you wanted to make a permanent installation of the programs/circuits, its a good idea to add two "pullup" 1K resistors - one resistor to connect between the SDA and 3.3V, and another resistor to connect between the SCL line to 3.3V.
If you are using a breadboard, this is easy enough to do and the addition of pullup resistors also helps to counteract any possible effects of stray capacitance between the breadboard lines which do lower the impedance between pins at high frequency (e.g. when frequency is set at 400,000).

## The "EIO" Error
This only happens with I2C device circuits. 

Whilst this error can occur if the sensor is just not connected up, I did find that the error also occurs in the following situation:
 - The sensor is wired up OK
 - I pressed Run (the program works OK)
 - I pressed "Ctrl/C" in Thonny to stop a program executing
 - I load/execute another program and the "EIO" error occurs just at the start (when executing the new program).

One way to fix this is to disconnect and reconnect the USB power cable to the PICO W and then press the red "stop/Restart" button in Thonny to reconnect the PICO W. This seems to reset things fine with the "EIO" error no longer happening thereafter. Of course, if you load/execute yet another program which uses a different I2C device, the error re-occurs and you have to repeat this annoying workaround fix. In effect you are switching the PICO W off and on

However, you also need to ensure you do the following while you are developing your code: 
 - If the memory in your PICO W already has "main.py", delete it from your PICO W (perhaps save it first). It may be that the version of "main.py" in your PICO W tries to immediately use an I2C device as soon as it is powered up, and it may be that your new program does not want to use that particular I2C device.  Removing "main.py" from your PICO W ensures that your PICO W boots up empty with regard to I2C devices
 - Disconnect and reconnect power to the PICO W (i.e. pull out and push back in the USB cable) and restart the backend in Thonny (press the red "Stop/Restart" button in the menu bar). 
 
I'm thinking that when you have decided on your final circuit arrangement (where the micropython program is no longer changing), this strange effect would thankfully not occur anymore.    

## PICO 2 W pinout (same as PICO W)

<img src="/images/pico_2_W_pinout.png" alt="PICO 2 W Pinout"/>

# THE PROGRAMS, HOW TO USE AND THEIR SEQUENCE

## Step 1 - Attach OLED and execute "oled_sh1106.py"  
<img src="/images/oled_1_3_SH1106.jpg" alt="OLED"/>

**oled_sh1106.py** tests the 1.3 OLED Display using a SH1106 driver instead of the SSD1306 driver

Attach 1.3 OLED module as follows
 - VDD          -> pin 37 (3v3_en)
 - GND          -> pin 38 (Gnd) 
 - SCL          -> pin 15 (GP11)
 - SDA          -> pin 14 (GP10)

## Step 2 - Attach GPS module and execute "gpsDisplay.py" 
<img src="/images/gps module.jpg" alt="GPS Module"/>

**gpsDisplay.py** tests both the GPS Module and the OLED

Attach GPS Module as follows
 - VCC          -> pin 37 (3v3_en)
 - RX           -> pin 11 (GP8)
 - TX           -> pin 12 (GP9)
 - GND          -> pin 38 (Gnd) 

## Step 3 - Attach BNO0055 and execute "bno055_test.py" 
<img src="/images/BNO055.jpg" alt="BNO055"/>

**bno055_test.py** tests the BNO055 module and outputs to serial

Attach BNO055 Module as follows
 - VIN          -> pin 37 (3v3_en)
 - GND          -> pin 38 (Gnd) 
 - SCL/Rx       -> pin 20 (GP15)
 - SDA/Tx       -> pin 19 (GP14)

## Step 4 - Attach BME280 and execute "bme280_test.py" 
<img src="/images/bme280.jpg" alt="BME280"/>

**bme280_test.py** tests the BME280 module and outputs to serial

Attach BME280 Module as follows
 - VIN          -> pin 37 (3v3_en)
 - GND          -> pin 38 (Gnd) 
 - SCL          -> pin 10 (GP7)
 - SDA          -> pin  9 (GP6)

## Other program 1 - "i2cScan.py"
**i2cScan.py** scans for any connected I2C modules. You do have to configure it to listen on various pin pairs.

## Other program 2 - "netScan.py"
**netScan.py** sniffs for wifi access points and lists any SSID found (It doesn't need any modules).

## Other program 3 - "uart.py"
**uart.py** is a general use UART (TX/RX) program. If it receives anything, it prints to serial. You can configure it to listen on various pin pairs and at different BAUD rates

## Other program 4 - "wifi_sta.py"
**wifi_sta.py** will set up a webserver page where you can control the onboard (green) LED on or off. You first need to modify the code in "secrets.py" with your SSID and SSID password. (It doesn't need any modules). When the program executes, it will try to connect to your wifi. If it connects, the serial window will display the IP address that has been assigned. Go to a web browser and enter this IP address (it will be something like http://192.168.1.XXX where you have to change the last three digits). This IP address will show a webpage with two buttons. If you press the appropriate button, you can switch the onboard green LED on and off. If you are changing the program and retesting, there is sometimes a socket error with this webpage. If you get this error, just delete the cache of your web browser, disconnect/reconnect the PICO W and wait 10 seconds. Also, be aware that there is supposed to be a limit of 4 people being able to access the webpage at the same time.

N.B. the webpage that you see, is parsed from "index.html". You can adapt "index.html" to show whatever you want, as long as the buttons still work

## Other program 5 - "weatherStation.py"
**weatherStation.py** will set up a webserver page where you can see the values coming from the BME280 module. If you haven't already done so, you first need to modify the code in "secrets.py" with your SSID and SSID password. When the program executes, it will try to connect to your wifi. If it connects, the serial window will display the IP address that has been assigned. Go to a web browser and enter this IP address (it will be something like http://192.168.1.XXX where you have to change the last three digits). If you are changing the program and retesting, there is sometimes a socket error with this webpage. If you get this error, just delete the cache of your web browser, disconnect/reconnect the PICO W and wait about 10 seconds. Also, be aware that there is supposed to be a limit of 4 people being able to access the webpage at the same time.

N.B. the webpage that you see, is parsed from "windex.html". You can adapt "windex.html" to show whatever you want. If you want to add more variables, look for how "%%i1" is treated in program "weatherStation.py", and where it is placed in "windex.html". The idea is that you put placeholder variables in the static html page source, and in the micropython program, the placeholder variables are replaced with the actual values. There is nothing special about using "%%i1" for a placeholder. I've only chosen that sequence of 4 characters because that sequence is unlikely to be elesewhere in the HTML file. Be aware that by using the "replace " command, all occurances of the placeholder variable will be replaced, so make sure there is a separately named placeholder variable for each bit you want to change.

N.B. The webpage will refresh every 5 seconds, as defined in the first line of the "windex.html"  ("meta http-equiv="refresh" content="5" )

## Other program 6 - "blink.py"
Does what it says - blinks the on-board LED

## Other program 7 - "catfacts.py"
This retrieves info about cats from the internet, and prints it out 
