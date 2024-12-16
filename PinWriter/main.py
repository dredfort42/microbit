from microbit import *

while True:
        # sleep(100)
    if button_a.was_pressed():
        display.show("1")
        pin16.write_digital(1)
        while button_b.was_pressed() == False:
            pin9.write_digital(0)
            pin1.write_digital(1)
            sleep(250)
            pin1.write_digital(0)
            pin9.write_digital(1)
            sleep(250)
        display.show("0")
        pin1.write_digital(1)
        pin9.write_digital(1)
        pin16.write_digital(0)




