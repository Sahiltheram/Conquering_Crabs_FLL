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
    gyro_turn(-45, left_motor, right_motor, gyro, walter)
    walter.straight(270)
    walter.straight(-165)
    gyro_turn(95, left_motor, right_motor, gyro, walter)
#change_shipping_lanes
    attach_left_motor.run_time(-700, 700, Stop.COAST, wait=True)
    walter.straight(75)
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
    gyro_turn(-65, left_motor, right_motor, gyro, walter)
    walter.straight(475)
    gyro_turn(-42, left_motor, right_motor, gyro, walter)
    walter.straight(30)
# do the radar
    claw_down(350, 192)
    walter.straight(-200)
# green sample mission
    claw_up(300, 150)
    gyro_turn(105, left_motor, right_motor, gyro, walter)
    walter.straight(-95)
    claw_down_coast(700, 98)
    wait(3000)
    gyro_turn(-30, left_motor, right_motor, gyro, walter)
    walter.straight(-20)
    gyro_turn(-54, left_motor, right_motor, gyro, walter)
    walter.straight(-1000)
