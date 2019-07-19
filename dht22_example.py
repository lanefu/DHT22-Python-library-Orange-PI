import OPi.GPIO as gpio
import logging

#import RPi.GPIO as GPIO
import dht22
import time
import datetime

# initialize GPIO
#gpio.setwarnings(False)
gpio.setboard(gpio.PRIME)
gpio.setmode(gpio.SOC)
#PIN2 = port.PA13
pin = gpio.PA + 10
#gpio.cleanup()

gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_OFF)
# read data using pin 14
instance = dht22.DHT22(pin)

while True:
    result = instance.read()
    if result.is_valid():
        fResult = ( result.temperature * (9 / 5) + 32)
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %.2f C" % result.temperature)
       #im an American
        print("Temperature: %.2f F" % fResult)
        print("Humidity: %.2f %%\n" % result.humidity)

    time.sleep(1)
