from microbit import *

steps=0

while True:
    if accelerometer.was_gesture('shake'):
        steps += 1
        display.show(steps)
    if button_a.was_pressed() or button_b.was_pressed():
        steps = 0
        display.clear()
        display.show(Image.DIAMOND)
        sleep(250)
        display.show(Image.DIAMOND_SMALL)
        sleep(250)
        display.clear()