from microbit import *

def on_button_pressed_a():
    display.clear_screen()
    for index in range(3):
        music.play(music.string_playable("C5 D A C C5 F C5 C ", 140),
            music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C D C D E A D C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    display.clear_screen()
    display.show_leds("""
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . . . #
        """)
    sleep(2000)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    sleep(5000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    basic.show_leds("""
        # # # . .
        # . # # #
        # # # # #
        # . # # #
        # # # . .
        """)
    sleep(2000)
    display.show_icon(IconNames.SILLY)
basic.forever(on_forever)
