from machine import UART, Pin

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9), bits=8, parity=None, stop=1)
#uart1.write(b'UART on GPIO8 & GPIO9 at 9600 baud\n\r')

#uart0 = UART(0)
#uart0.write(b'UART on GPIO0 & GPIO1 at 115200 baud\n\r')



while True:
    rec = False
    rxData = bytes()
    while uart1.any() > 0:
        rec = True
        rxData += uart1.read()
    if rec == True:
        rec = False
#        text1 = rxData.decode()
#        print(rxData.decode())
        myarr = rxData.decode().split("\n")
        print(myarr[2])