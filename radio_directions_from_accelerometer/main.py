from microbit import *
import radio

radio.config(group=1)
radio.on()

isController = False

def sendDirection():
    if accelerometer.was_gesture('up'):
        radio.send('up')
        display.show(Image.ARROW_S)
    if accelerometer.was_gesture('down'):
        radio.send('down')
        display.show(Image.ARROW_N)
    if accelerometer.was_gesture('left'):
        radio.send('left')
        display.show(Image.ARROW_W)
    if accelerometer.was_gesture('right'):
        radio.send('right')
        display.show(Image.ARROW_E)
     
def receiveDirection(message):
    if message == 'up':
        radio.send('ok')
        display.show(Image.ARROW_S)
    if message == 'down':
        radio.send('ok')
        display.show(Image.ARROW_N)
    if message == 'left':
        radio.send('ok')
        display.show(Image.ARROW_W)
    if message == 'right':
        radio.send('ok')
        display.show(Image.ARROW_E)
    
while True:
    message = radio.receive()

    if message == 'newController':
        isController = False
        for i in range(2):
            display.show(Image.ARROW_S)
            sleep(250)
            display.show(Image.ARROW_W)
            sleep(250)
            display.show(Image.ARROW_N)
            sleep(250)
            display.show(Image.ARROW_E)
            sleep(250)
        display.clear()
    if message == 'ok':
        sleep(250)
        display.show(Image.YES)
        sleep(250)
        display.clear()
    if button_a.was_pressed() or button_b.was_pressed():
        isController = True
        radio.send('newController')
        for i in range(4):
            display.show(Image.HOUSE)
            sleep(300)
            display.clear()
            sleep(200)
    
    if isController == True:
        sendDirection()
    else:
        receiveDirection(message)