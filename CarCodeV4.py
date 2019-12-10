from microbit import *

display.off()  #Turns the microbit display off so we can use the display pins in this build. 

user_input = []  # This is the list of user input commands, it is empty, but it will get filled when the user uses the code

gmA1 = pin0  # Pin aliasing 
bmA2 = pin1

wmB1 = pin12
bmB2 = pin8


bForward = pin2
bBackwards = pin10
bRight = pin3
bLeft = pin7
bStart = pin6


# This turns both the motors on for a given time, while simultaiously turning the LED on - to display that it is in progress
# It takes positive numbers for forwards, and negative numbers for Backwards
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

    
# This short function blinks the LED 
def blink():
    pin13.write_digital(1)
    sleep(75)
    pin13.write_digital(0)


# This function turns the car a given angle - if the button is pushed for 1 second, it turns at 45 degrees
# If the button was pushed for longer than 2 seconds, it turns 90 degrees 
# It uses positive for left turns, and negative for right turns.
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

# this function records the user input, and takes input of which pins to read, and what direction. - given later in the program
def record(x, y):

    i = 0
    while x.read_digital():  # Gets the number of seconds the user pressed 'FORWARD'
        i += 1
        blink()
        sleep(1000)
    user_input.append((y, i))

    
# This code block is the only thing running on the microbit 
# It checks for specific pin-Highs, and reads them, and then sends them to the record function.

while True:

    if bForward.read_digital():
        record(bForward, "F")
    if bBackwards.read_digital():
        record(bBackwards, "B")
    if bLeft.read_digital():
        record(bLeft, "L")
    if bRight.read_digital():
        record(bRight, "R")

    # This block of code is run when the start button is pushed, 
    # It reads the list (user_input) and looks at each tuple of it.
    # depending on what direction is assigned, it will send the time to a different function 
    # This is the movement part.
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
