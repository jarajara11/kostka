cislo = 0

def on_gesture_shake():
    global cislo
    cislo = randint(1, 6)
    if cislo == 1:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    elif cislo == 2:
        basic.show_leds("""
            # # . . .
            # # . . .
            . . . . .
            . . . # #
            . . . # #
            """)
    elif cislo == 3:
        basic.show_leds("""
            . . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . .
            """)
    elif cislo == 4:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    elif cislo == 5:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
    else:
        basic.show_leds("""
            # . . . #
            . . . . .
            # . . . #
            . . . . .
            # . . . #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
