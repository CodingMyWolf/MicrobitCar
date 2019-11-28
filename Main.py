from microbit import *

# ------------VARIABLES-----------------------------------------
# In code Variables
user_input = []  # This is the list of instructions from the user - it starts empty, and fills up as buttons are pressed


# Pin aliasing - Just labeling pins to more convenient names

# Motors
fmotor = pin0  # Forward output
bmotor = pin1  # Backwards output
rmotor = pin13  # Right output
lmotor = pin14  # Left output

# Servos - To be added at some point
# steer = pin__

# Buttons (UI)
bForward = pin2  # Forward input
bBackwards = pin16  # Backwards input
bLeft = button_a  # Left input
bRight = button_b  # Right input
bPause = pin15  # Pause input
bGo = pin8  # Start input
#bSpeed = pin__  # May be added later
# ----------------OBJECTS-------------------------


def forward(time):  # Moves the car forward
    for i in range(0, time):
        fmotor.write_digital(1)
        sleep(1000)
    fmotor.write_digital(0)


def backward(time):  # Moves the car backwards
    for i in range(0, time):
        bmotor.write_digital(1)
        sleep(1000)
    bmotor.write_digital(0)


def pause(time):  # Creates a pause in the driving sequence where car stops for set amount of time
    for i in range(0, time):
        sleep(1000)


def left_turn(angle):  # Turns the car left
    lmotor.write_digital(1)
    if angle == 30:
        forward(2)   # Needs to be based on the turn radius of the car - Motor speed. edit number of seconds.
    else:
        forward(4)
    lmotor.write_digital(0)


def right_turn(angle):  # Turns the car right
    rmotor.write_digital(1)
    if angle == 30:
        forward(2)   # Needs to be based on the turn radius of the car
    else:
        forward(4)
    rmotor.write_digital(0)


def compute_angle(sec):  # Takes a time input and turns it into an angle output for the other functions
    if sec <= 1:
        return 30
    else:
        return 90


def return_speed():  # !!! - This could modulate the speed - might be added later
    pass

# -------------MAIN CODE BLOCK---------------------------------------------

# Disabling I2C Feature


# This series of statements takes the user input, and compiles it into a list of tuples.
# These while statements read the number of seconds the buttons were held, and adds that to the list of instructions

while True:

    if bForward.read_digital():

        f = 0
        while bForward.read_digital():  # Gets the number of seconds the user pressed 'FORWARD'
            f += 1
            sleep(1000)

        user_input.append(("F", f))

    if bBackwards.read_digital():

        b = 0
        while bBackwards.read_digital():  # Gets the number of seconds the user pressed 'BACKWARDS'
            b += 1
            sleep(1000)

        user_input.append(("B", b))

    if bLeft.is_pressed():

        l = 0
        while bLeft.is_pressed():  # Gets the number of seconds the user pressed 'LEFT'
            l += 1
            sleep(1000)
        l = compute_angle(l)

        user_input.append(("L", l))

    if bRight.is_pressed():

        r = 0
        while bRight.is_pressed():  # Gets the number of seconds the user pressed 'RIGHT'
            r += 1
            sleep(1000)
        r = compute_angle(r)
        user_input.append(("R", r))

    if bPause.read_digital():

        p = 0
        while bPause.read_digital():  # Gets the number of seconds the user pressed 'PAUSE'
            p += 1
            sleep(1000)
        user_input.append(("P", p))

    # ----------------------------------SEPARATE FUNCTION---------------------------------------------------
    # This statement tells the motors what to do - After the start button is pushed.
    # It will decipher the list of instructions, and call the correct functions to move the car in that order
    # After all functions have been accomplished, it will clear the list so the process can start over.

    if bGo.read_digital():

        sleep(1000)

        for element in user_input:

            e = element[0]
            t = element[1]

            if e == "F":
                forward(t)
            if e == "B":
                backward(t)
            if e == "L":
                left_turn(t)
            if e == "R":
                right_turn(t)
            if e == "P":
                pause(t)

        user_input.clear()
