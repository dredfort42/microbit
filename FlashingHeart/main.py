from microbit import *
from initialTester import *

tester("TEST")

for i in range(3):
    display.show(Image.CHESSBOARD)
    sleep(500)
    display.clear()
    sleep(500)

while True:
    if (button_a.was_pressed()):
        break
    else:
        display.show(Image.HEART_SMALL)
        sleep(400)
        display.clear()
        sleep(10)
        display.show(Image.HEART)
        sleep(600)
        display.clear()
        sleep(500)
    