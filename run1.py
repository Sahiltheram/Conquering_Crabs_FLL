from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from move_functions import *
from gyro_turn import gyro_turn



def run1 (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro):
#unexpected encounter
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    walter.straight(280)
    gyro_turn(-51, left_motor, right_motor, gyro, walter)
    walter.straight(240)
    walter.straight(-165)
    gyro_turn(85, left_motor, right_motor, gyro, walter)
#change_shipping_lanes
    attach_left_motor.run_time(-700, 700, Stop.COAST, wait=True)
    walter.straight(115)
    attach_left_motor.run_angle(300, 35, Stop.HOLD, True)
    wait(1000)
    walter.stop()
    gyro_turn(20, left_motor, right_motor, gyro, walter)
    walter.straight(-50)
    attach_left_motor.run_angle(75, -10, Stop.COAST, wait=True)
    ev3.speaker.beep(500,200)
    walter.straight(-50)
    attach_left_motor.run_angle(300, 180, Stop.COAST, wait=True)
#get_the_krill
    walter.turn(-55)
    walter.straight(400)
    gyro_turn(-16.99, left_motor, right_motor, gyro, walter)
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