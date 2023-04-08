from machine import ADC, Pin, SoftI2C
from neopixel import NeoPixel
from lib.scd4x import SCD4X
from lib.sh1107 import SH1107, SH1107_I2C
import lib.aiorepl as aiorepl
import json
import struct
import network
import urequests
import bluetooth
from micropython import const
import machine
import picoweb
from machine import Pin
import gettime
import time

try:
    import uasyncio as asyncio
except Exception as ex:
    import asyncio

OFF = (0,0,0)
BLUE = (0, 0, 8)
GREEN = (0, 8, 0)
YELLOW = (4, 4, 0)
ORANGE = (6, 3, 0)
RED = (8, 0, 0)
SSID = "hi"
PASSWORD = "12345678"

try:
    with open('config.json', "r") as config_file:
        config = json.load(config_file)
except Exception as e:
    print("While parsing config.json: " + str(e))
    config = {}
del config

red = Pin(13, Pin.OUT)
green = Pin(27, Pin.OUT)
lumi_sensor = ADC(Pin(33))
rgb_leds = NeoPixel(Pin(25), 3)
i2c = SoftI2C(sda=Pin(23), scl=Pin(22))

try:
    scd4x = SCD4X(i2c)
    scd4x.start_periodic_measurement()
except Exception as ex:
    print("Error: SCD41 sensor is not connected " + str(ex))
    scd4x = None

try:
    display = SH1107_I2C(128, 64, i2c)
except Exception as ex:
    print("Error: SH1107 is not connected, or maybe RST button is constantly pressed?" + str(ex))
    display = None

button_a = Pin(14, Pin.IN) # works. lowest button: 0 when pressed
button_c = Pin(15, Pin.IN) # works. highest button: 0 when pressed.



station = network.WLAN(network.STA_IF)

if station.isconnected():
  green.value(1)
else:
  red.value(1)
  
  
def show(time,temp,ip):
    """ display data on the OLED"""
    try:
        display = SH1107_I2C(128, 64, i2c)
    except Exception as ex:
        print("Error: SH1107 is not connected, or maybe RST button is constantly pressed?" + str(ex))
    display.fill(0)
    display.text(f"{time}" , 0, 9, 1)
    display.text(temp , 0, 18, 1)
    display.text(ip , 0, 54, 1)
    display.show()

t="no data"
if scd4x.temperature:
  t= str(round(scd4x.temperature,2)) + " *C"

show(gettime.get_time(), t, station.ifconfig()[0])
  


ip=[]
app = picoweb.WebApp(__name__)

def qs_parse(qs):
  parameters = {}
  ampersandSplit = qs.split("&")
  
  for element in ampersandSplit:
    equalSplit = element.split("=")
  parameters[equalSplit[0]] = equalSplit[1]
  return parameters




@app.route('/api/temperature')
def temp(req, resp):
  temp="no data"
  if scd4x.temperature:
    temp= str(round(scd4x.temperature,2)) + " *C"
  show(gettime.get_time(), temp, station.ifconfig()[0])
  temp={"temp":temp,"date":gettime.get_time()}
  yield from picoweb.jsonify(resp, temp)

@app.route('/api/presence')
def presence(req, resp):
  presence={}
  with open('p_data.json', "r") as f:
    presence = json.load(f)
  yield from picoweb.jsonify(resp, presence)
  
  
if __name__ == "__main__":
  app.run(debug=True,host="0.0.0.0",port=80)
