# Motors
fmotor = pin0
bmotor = pin1
lmotor = pin2
rmotor = pin3

# Buttons (UI)
bForward = pin4
bBackwards = pin5
bLeft = pin6
bRight = pin7
bGo = pin8
bSpeed = pin10
# ----------------OBJECTS-------------------------


def forward(time):  # Moves the car forward
    for i in range(0, time):
        fmotor.write_digital(1)
        sleep(1000)


def backward(time):  # Moves the car backwards
    for i in range(0, time):
        bmotor.write_digital(1)
        sleep(1000)


def left_turn(angle):  # Turns the car left
    lmotor.write_digital(1)
    forward(angle)


def right_turn(angle):  # Turns the car right
    rmotor.write_digital(1)
    forward(angle)


def compute_angle(sec):  # !!!
    return sec+1


def return_speed():  # !!!
    return bSpeed.read_analog()

# -------------MAIN CODE BLOCK---------------------------------------------


# This series of statements takes the user input, and compiles it into a list of tuples.
# These while statements read the number of seconds the buttons were held, and adds that to the list of instructions
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

if bLeft.read_digital():

    l = 0
    while bLeft.read_digital():  # Gets the number of seconds the user pressed 'LEFT'
        l += 1
        sleep(1000)

    user_input.append(("L", l))

if bRight.read_digital():

    r = 0
    while bRight.read_digitali():  # Gets the number of seconds the user pressed 'RIGHT'
        r += 1
        sleep(1000)

    user_input.append(("R", r))

# ----------------------------------SEPARATE FUNCTION---------------------------------------------------
# This statement tells the motors what to do - After the start button is pushed.

if bGo.read_digital():

    sleep(5000)

    for element in user_input:

        e = element[0]
        t = element[1]

        if e == "F":
            forward(t)
        elif e == "B":
            backward(t)
        elif e == "L":
            left_turn(t)
        elif e == "R":
            right_turn(t)
