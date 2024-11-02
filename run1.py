from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from move_functions import *



def run1 (ev3, walter, left_motor, right_motorattach_left_motor, attach_right_motor, gyro):
#unexpected encounter
    walter.straight(280)
    walter.turn(-55)
    walter.straight(185)
    wait(5000)
    walter.straight(-165)
    walter.turn(50)
#krill_numero_uno
    walter.straight(71)
    walter.turn(52.5)
#change_shipping_lanes
    attach_left_motor.run_time(-700, 700, Stop.COAST, wait=True)
    walter.straight(50)
    attach_left_motor.run_angle(300, 30, Stop.HOLD, wait=True)
    walter.turn(45)
    attach_left_motor.run_angle(75, -10, Stop.COAST, wait=True)
    ev3.speaker.beep(500,200)
    walter.straight(-50)
    attach_left_motor.run_angle(300, 180, Stop.COAST, wait=True)
#get_the_krill
    walter.turn(-70)
    walter.straight(400)
    # walter.straight(-180)
    # walter.turn(-60)
    # walter.straight)
    # walter.turn(-70)
    # walter.straight(100)
    # wait(1000)
    # claw_down(left_motor, 100, 180)
    # wait(1000)
    # walter.straight(-200)

#radar    
    # walter.turn(25)
    # wait(3000)
    # walter.straight(100)
    # attach_right_motor.run_angle(300, 80, Stop.COAST, wait=TRUE)
    
   
    
    
    #walter.straight(-10)
    #walter.turn(165)
    #walter.straight(100)
    #walter.straight(-200)
    #walter.turn(85)
    #walter.straight(350)