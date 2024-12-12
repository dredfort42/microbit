from microbit import *

display.show(Image('00000:'
                   '00000:'
                   '00300:'
                   '00000:'
                   '00000'))
sleep(200)

display.show(Image('00000:'
                   '00300:'
                   '03630:'
                   '00300:'
                   '00000'))
sleep(200)

display.show(Image('00300:'
                   '03630:'
                   '36963:'
                   '03630:'
                   '00300'))
sleep(200)

display.show(Image('03630:'
                   '36963:'
                   '69696:'
                   '36963:'
                   '03630'))
sleep(200)

display.show(Image('36963:'
                   '69696:'
                   '96369:'
                   '69696:'
                   '36963'))
sleep(200)

display.show(Image('69696:'
                   '96369:'
                   '63036:'
                   '96369:'
                   '69696'))
sleep(200)

display.show(Image('96369:'
                   '63036:'
                   '30003:'
                   '63036:'
                   '96369'))
sleep(200)

display.show(Image('63036:'
                   '30003:'
                   '00000:'
                   '30003:'
                   '63036'))
sleep(200)

display.show(Image('30003:'
                   '00000:'
                   '00000:'
                   '00000:'
                   '30003'))
sleep(200)
    
display.clear()

# compass.calibrate()

sector = 360/8
start = 360 - (sector/2)
stop = (sector/2)

while True:
    d = compass.heading()
    
    if (d > start and d <= 360) or (d >= 0 and d <= stop):
        display.show(Image.ARROW_N)
    if d > start + 1*sector - 360  and d <= stop + 1*sector:
        display.show(Image.ARROW_NE)
    elif d > start + 2*sector - 360 and d <= stop + 2*sector:
        display.show(Image.ARROW_E)
    elif d > start + 3*sector - 360 and d <= stop + 3*sector:
        display.show(Image.ARROW_SE)
    elif d > start + 4*sector - 360 and d <= stop + 4*sector:
        display.show(Image.ARROW_S)
    elif d > start + 5*sector - 360 and d <= stop + 5*sector:
        display.show(Image.ARROW_SW)
    elif d > start + 6*sector - 360 and d <= stop + 6*sector:
        display.show(Image.ARROW_W)
    elif d > start + 7*sector - 360 and d <= stop + 7*sector:
        display.show(Image.ARROW_NW)
    