from microbit import*
user_input=[]
fmotor=pin0
bmotor=pin1
rmotor=pin13
lmotor=pin14
bForward=pin2
bBackwards=pin16
bLeft=button_a
bRight=button_b
bPause=pin15
bGo=pin8
def forward(time): 
 for i in range(0,time):
  fmotor.write_digital(1)
  sleep(1000)
 fmotor.write_digital(0)
def backward(time): 
 for i in range(0,time):
  bmotor.write_digital(1)
  sleep(1000)
 bmotor.write_digital(0)
def pause(time):
 for i in range(0,time):
  sleep(1000)
def left_turn(angle): 
 lmotor.write_digital(1)
 if angle==30:
  forward(2) 
 else:
  forward(4)
 lmotor.write_digital(0)
def right_turn(angle): 
 rmotor.write_digital(1)
 if angle==30:
  forward(2) 
 else:
  forward(4)
 rmotor.write_digital(0)
def compute_angle(sec): 
 if sec<=1:
  return 30
 else:
  return 90
def return_speed(): 
 pass
while True:
 if bForward.read_digital():
  f=0
  while bForward.read_digital(): 
   f+=1
   sleep(1000)
  user_input.append(("F",f))
 if bBackwards.read_digital():
  b=0
  while bBackwards.read_digital(): 
   b+=1
   sleep(1000)
  user_input.append(("B",b))
 if bLeft.is_pressed():
  l=0
  while bLeft.is_pressed(): 
   l+=1
   sleep(1000)
  l=compute_angle(l)
  user_input.append(("L",l))
 if bRight.is_pressed():
  r=0
  while bRight.is_pressed(): 
   r+=1
   sleep(1000)
  r=compute_angle(r)
  user_input.append(("R",r))
 if bGo.read_digital():
  sleep(1000)
  for element in user_input:
   e=element[0]
   t=element[1]
   if e=="F":
    forward(t)
   if e=="B":
    backward(t)
   if e=="L":
    left_turn(t)
   if e=="R":
    right_turn(t)
  user_input.clear()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
