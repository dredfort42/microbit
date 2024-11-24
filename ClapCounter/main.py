from microbit import *

microphone.set_threshold(SoundEvent.LOUD, 125)

clapCount = 0
display.show(Image.HEART_SMALL)
sleep(500)
display.show(Image.HEART)
sleep(500)
display.clear()
sleep(500)

while True:
    if microphone.was_event(SoundEvent.LOUD):
        clapCount = clapCount + 1

    if clapCount > 0:
        display.scroll(clapCount)

    if button_a.was_pressed():
        # if clapCount > 0:
            for i in range(3):
                display.show(Image(
                    '99999:'
                    '90009:'
                    '90009:'
                    '90009:'
                    '99999'
                ))
                sleep(225)
                display.show(Image(
                    '77777:'
                    '79997:'
                    '79097:'
                    '79997:'
                    '77777'
                ))
                sleep(200)
                display.show(Image(
                    '55555:'
                    '57775:'
                    '57975:'
                    '57775:'
                    '55555'
                ))
                sleep(175)
                display.show(Image(
                    '00000:'
                    '05550:'
                    '05750:'
                    '05550:'
                    '00000'
                ))
                sleep(150)
                display.show(Image(
                    '00000:'
                    '00000:'
                    '00500:'
                    '00000:'
                    '00000'
                ))
                sleep(125)
                display.clear()
                sleep(100)
            
            clapCount = 0
