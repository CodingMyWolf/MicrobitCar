from microbit import *

display.off()

user_input = []

gmA1 = pin0
bmA2 = pin1

wmB1 = pin12
bmB2 = pin8


bForward = pin2
bBackwards = pin10
bRight = pin3
bLeft = pin7
bStart = pin6


def both_motors_on(time):
    pin13.write_digital(1)
    if time >= 0:

        for i in range(0, time):
            gmA1.write_digital(1)
            bmA2.write_digital(0)
            wmB1.write_digital(1)
            bmB2.write_digital(0)
            sleep(1000)
        gmA1.write_digital(0)
        bmA2.write_digital(0)
        wmB1.write_digital(0)
        bmB2.write_digital(0)
    else:
        time = time*(-1)
        for i in range(0, time):
            gmA1.write_digital(0)
            bmA2.write_digital(1)
            wmB1.write_digital(0)
            bmB2.write_digital(1)
            sleep(1000)
        gmA1.write_digital(0)
        bmA2.write_digital(0)
        wmB1.write_digital(0)
        bmB2.write_digital(0)
    pin13.write_digital(0)

def blink():
    pin13.write_digital(1)
    sleep(75)
    pin13.write_digital(0)


def turn(angle):
    pin13.write_digital(1)
    if angle >= 0:
        time = 375 if angle == 1 else 750
        gmA1.write_digital(1)
        bmA2.write_digital(0)
        sleep(time)
        gmA1.write_digital(0)
    else:
        angle = angle * (-1)
        time = 375 if angle == 1 else 750
        wmB1.write_digital(1)
        bmB2.write_digital(0)
        sleep(time)
        wmB1.write_digital(0)
    pin13.write_digital(0)


def record(x, y):

    i = 0
    while x.read_digital():  # Gets the number of seconds the user pressed 'FORWARD'
        i += 1
        blink()
        sleep(1000)
    user_input.append((y, i))


while True:

    if bForward.read_digital():
        record(bForward, "F")
    if bBackwards.read_digital():
        record(bBackwards, "B")
    if bLeft.read_digital():
        record(bLeft, "L")
    if bRight.read_digital():
        record(bRight, "R")

    if bStart.read_digital():

        sleep(500)
        for element in user_input:
            e = element[0]
            t = element[1]

            if e == "F":
                both_motors_on(t)
            if e == "B":
                both_motors_on(-t)
            if e == "L":
                turn(t)
            if e == "R":
                turn(-t)
        user_input.clear()
