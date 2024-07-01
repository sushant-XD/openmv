# Untitled - By: asus - Mon Jul 1 2024

import sensor, image, time, machine

RED_LED_PIN = 1
BLUE_LED_PIN = 3
GREEN_LED_PIN = 2

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    pyb.LED(RED_LED_PIN).on()
    pyb.delay(4000);
    pyb.LED(RED_LED_PIN).off()
    pyb.delay(4000)
    pyb.LED(BLUE_LED_PIN).on()
    pyb.delay(4000);
    pyb.LED(BLUE_LED_PIN).off()
    pyb.delay(4000)
    pyb.LED(GREEN_LED_PIN).on()
    pyb.delay(4000)
    pyb.LED(GREEN_LED_PIN).off()
    pyb.delay(4000)
    
