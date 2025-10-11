# Copyright (c) 2025 MTHS All rights reserved
#
# Created by: Isaac Ip
# Created on: Oct 2025
# This program reads in the amount of light.

from microbit import *
import neopixel

# variables
amountOfLight = 0
neopixelStrip = neopixel.NeoPixel(pin16, 4)

# cleanup
display.clear()
neopixelStrip[0] = (0, 0, 0)
neopixelStrip[1] = (0, 0, 0)
neopixelStrip[2] = (0, 0, 0)
neopixelStrip[3] = (0, 0, 0)
neopixelStrip.show()
display.show(Image.HAPPY)

# light up leds
while True:
    if button_a.is_pressed():

        # get light level
        amountOfLight = display.read_light_level()

        # show light level
        display.show(str(amountOfLight))
        sleep(1000)
        display.clear()

        if amountOfLight <= 51:
            neopixelStrip[0] = (0, 0, 0)
            neopixelStrip[1] = (0, 0, 0)
            neopixelStrip[2] = (0, 0, 0)
            neopixelStrip[3] = (0, 0, 0)
            neopixelStrip.show()

        # light up 1 led
        if amountOfLight > 52:
            neopixelStrip[0] = (255, 255, 255)
            neopixelStrip.show()

        # light up 2 leds
        if amountOfLight > 104:
            neopixelStrip[0] = (255, 255, 255)
            neopixelStrip[1] = (255, 255, 255)
            neopixelStrip.show()

        # light up 3 leds
        if amountOfLight > 156:
            neopixelStrip[0] = (255, 255, 255)
            neopixelStrip[1] = (255, 255, 255)
            neopixelStrip[2] = (255, 255, 255)
            neopixelStrip.show()

        # light up 4 leds
        if amountOfLight > 208:
            neopixelStrip[0] = (255, 255, 255)
            neopixelStrip[1] = (255, 255, 255)
            neopixelStrip[2] = (255, 255, 255)
            neopixelStrip[3] = (255, 255, 255)
            neopixelStrip.show()

        sleep(2000)
        neopixelStrip[0] = (0, 0, 0)
        neopixelStrip[1] = (0, 0, 0)
        neopixelStrip[2] = (0, 0, 0)
        neopixelStrip[3] = (0, 0, 0)
        neopixelStrip.show()
        display.show(Image.HAPPY)
