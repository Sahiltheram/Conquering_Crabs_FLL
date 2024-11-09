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
    walter.settings(600, 400, 300, 115)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    walter.straight(280)
    gyro_turn(-50, left_motor, right_motor, gyro, walter)
    walter.straight(270)
    walter.straight(-165)
    gyro_turn(92.5, left_motor, right_motor, gyro, walter)
#change_shipping_lanes
    attach_left_motor.run_time(-700, 700, Stop.COAST, wait=True)
    walter.straight(95)
    attach_left_motor.run_angle(300, 35, Stop.HOLD, True)
    wait(1000)
    gyro_turn(20, left_motor, right_motor, gyro, walter)
    walter.stop()
    walter.straight(-60)
    wait(1000)
    attach_left_motor.run_angle(75, -10, Stop.COAST, wait=True)
    ev3.speaker.beep(500,200)
    walter.straight(-50)
    attach_left_motor.run_angle(300, 180, Stop.COAST, wait=True)
# move towards radar
    walter.turn(-65)
    walter.straight(475)
    walter.turn(-51)
    walter.straight(30)
# do the radar
    claw_down(attach_left_motor, 350, 200)
    walter.straight(-200)
# green sample mission
    walter.stop()
    claw_up(attach_left_motor, 300, 35)
    wait(2000)
    walter.reset()
    walter.drive(-80, 90)
    while (walter.distance() > -160) and (walter.angle() < 180):
        wait(1)
    walter.straight(-50)
    walter.stop()
    
    # right_motor.run_angle(200, -395)
    # walter.straight(-20)
    # claw_down(attach_left_motor, 350, 20)
    