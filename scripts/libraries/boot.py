# Untitled - By: asus - Mon Jul 1 2024

import sensor, image, time, machine

RED_LED_PIN = 1

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    pyb.LED(RED_LED_PIN).on()
    pyb.delay(1000);
    pyb.LED(RED_LED_PIN).off()
