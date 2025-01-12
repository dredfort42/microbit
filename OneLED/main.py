from microbit import *

while True:
    pin0.write_digital(1)
    display.show(Image.CHESSBOARD)
    sleep(500)
    pin0.write_digital(0)
    display.clear()
    sleep(500)
