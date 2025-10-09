/* Copyright (c) 2025 MTHS All rights reserved
 *
 * Created by: Isaac Ip
 * Created on: Oct 2025
 * This program reads in the amount of light.
*/

//variables
let lightLevel = 0
let neopixelStrip: neopixel.Strip = null

//cleanup
basic.clearScreen()
neopixelStrip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
neopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.setPixelColor(2, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.setPixelColor(3, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.show()
basic.showIcon(IconNames.Happy)

lightLevel = input.lightLevel()

//light up nothing
if (lightLevel <= 51) {
    // show nothing
}

// light up 1 led
if (lightLevel > 52) {
    neopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.White))
    neopixelStrip.show()
}

// light up 2 leds
if (lightLevel > 104) {
    neopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.White))
    neopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.White))
    neopixelStrip.show()
}

// light up 3 leds
if (lightLevel > 156) {
    neopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.White))
    neopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.White))
    neopixelStrip.setPixelColor(2, neopixel.colors(NeoPixelColors.White))
    neopixelStrip.show()
}

// light up 4 leds
if (lightLevel > 208) {
    neopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.White))
    neopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.White))
    neopixelStrip.setPixelColor(2, neopixel.colors(NeoPixelColors.White))
    neopixelStrip.setPixelColor(3, neopixel.colors(NeoPixelColors.White))
    neopixelStrip.show()
}






