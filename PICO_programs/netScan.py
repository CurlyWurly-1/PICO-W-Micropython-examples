import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print(wlan.scan())