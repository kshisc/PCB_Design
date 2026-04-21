#Teammates: I worked alone

import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_treshold=100  # change this value
sound_treshold=500 # change this value


while True: 
  time.sleep(0.5) 

  #blink LED
  for i in range (5):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.5) 
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.5) 

  #read light sensor
  for i in range (50):
    light = mcp.read_adc(0)
    print(light)

    if light < lux_treshold:
      print("dark")
    else:
      print("bright")
    time.sleep(0.1) 

  #blink LED  
  for i in range (4):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.2) 
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.2) 

  #read sound sensor
  for i in range (50):
    sound = mcp.read_adc(1)
    print(sound)

    if sound > sound_treshold:
      GPIO.output(11, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(11, GPIO.LOW)
  
