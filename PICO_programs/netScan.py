import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
scnRecs = wlan.scan()
scnRecs.sort()
for scnRec in scnRecs:
    if scnRec[0].decode():
        print(f'{scnRec[0].decode():<25}{str(scnRec[1]):<40}')
