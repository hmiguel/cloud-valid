#!/usr/bin/python3

import RPi.GPIO as gpio
import time
import xenakis

gpo_pin = 4

gpio.setmode(gpio.BCM) # GPIO NUMBER
gpio.setup(gpo_pin, gpio.IN, pull_up_down=gpio.PUD_UP) # start at '1', pulled down on RF_INTERRUPT

def write_tag(data):
    write_ok = False
    # write tag here => todo
    return write_ok == True

def gpo_callback(channel):
    print ("ST25DV GPO detected on GPIO {pin}".format(pin = gpo_pin))
    info = xenakis.pack(xenakis.get_info())
    if (write_tag(info)):
    	print("Tag Updated!")

gpio.add_event_detect(gpo_pin, gpio.FALLING, callback=gpo_callback, bouncetime=200)

try:
    print ("Waiting for rising edge on GPIO {pin}".format(pin = gpo_pin))
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print ("\nExiting...")
finally:
    gpio.cleanup()           # clean up GPIO on normal exit
