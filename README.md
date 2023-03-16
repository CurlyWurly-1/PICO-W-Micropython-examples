# PICO-W--Micropython-examples-
For the RP2040 W - A collection of Micropython programs  

<img src="/images/picow_pinout.png" alt="PICO W Pinout"/>


# Step 1 - Attach OLED and execute "oled_sh1106.py"  (Test OLED - 1.3 OLED Display that uses SH1106 driver instead of SSD1306 driver) 
Attach 1.3 OLED module as follows
 - 3.3V power   -> pin 37 (3v3_en)
 - Grnd         -> pin 38 (Gnd) 
 - SDA          -> pin  1 (GP0)
 - SCL          -> pin  2 (GP1)

# Step 2 - Attach GPS module and execute "gpsDisplay.py" (Test GPS Module and OLED)
Attach GPS Module as follows
 - 3.3V power   -> pin 37 (3v3_en)
 - Grnd         -> pin 38 (Gnd) 
 - RX           -> pin 11 (GP8)
 - TX           -> pin 12 (GP9)

# Step 3 - Attach BNO0055 and execute "bno055_test.py" (Test Gyro sensor and OLED)
Attach BNO055 module as follows
 - 3.3V power   -> pin 37 (3v3_en)
 - Grnd         -> pin 38 (Gnd) 
 - SDA          -> pin 19 (GP14)
 - SCL          -> pin 20 (GP15)
