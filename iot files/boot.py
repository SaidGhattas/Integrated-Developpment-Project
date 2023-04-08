#runs on boot
import network
import esp
import ntptime
esp.osdebug(None)
import gc
gc.collect()
ssid='hi'
password='12345678'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass
ntptime.settime()
print('Connection successful')
print(station.ifconfig())

