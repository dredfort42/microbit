from microbit import *

Moisture = 0
Check_ready = True

def on_button_pressed_a():
    pin2.write_digital(1)
    sleep(2000)
    pin2.write_digital(0)

def on_button_pressed_b():
    global Moisture
    Moisture = pin0.read_analog()
    display.scroll(str((Moisture))) 

def check_moisture():
    global Check_ready
    if Check_ready:
        Check_ready = False
        Moisture = pin0.read_analog()
        if Moisture > 400:
            pin2.write_digital(1)
            sleep(2000)
            pin2.write_digital(0)
        
        display.scroll(str((Moisture)))
        sleep(5000)
        Check_ready = True

display.show(Image.HAPPY)
sleep(2000)
display.clear

while True:
    if button_a.was_pressed():
        on_button_pressed_a()
    elif button_b.was_pressed():
        on_button_pressed_b()
    else:
        check_moisture()
        


