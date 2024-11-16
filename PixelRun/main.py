from microbit import *

speed = 100
speedStep = 25

def readButtons():
    global speed
    if button_a.was_pressed():
        speed += speedStep
    if button_b.was_pressed():
        if speed > speedStep:
            speed -= speedStep
    print(speed)
        
w = 5
h = 5 
reverse = False
brightness = 1
iter = 0
        
while True:
    for i in range(w):
        for j in range(h):
            display.set_pixel(j, i, brightness)
            readButtons()
            sleep(speed)
    
    if brightness == 9:
        reverse = True
    
    if brightness == 0:
        reverse = False
    

    if reverse == False:
        brightness += 1
    else:
        brightness -= 1
    
    
