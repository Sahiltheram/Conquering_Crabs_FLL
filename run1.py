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
    walter.settings(600, 350, 300, 115)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    walter.straight(295)
    gyro_turn(-45, left_motor, right_motor, gyro, walter)
    walter.straight(270)
    walter.straight(-165)
    gyro_turn(92, left_motor, right_motor, gyro, walter)
#change_shipping_lanes
    attach_left_motor.run_time(-700, 700, Stop.COAST, wait=True)
    print(gyro.angle())
    walter.straight(57)
    attach_left_motor.run_angle(300, 8, Stop.HOLD, True)
    walter.straight(18)
    attach_left_motor.run_angle(300, 30, Stop.HOLD, True)
    wait(1000)
    print(gyro.angle())
    gyro_turn(20, left_motor, right_motor, gyro, walter)
    print(gyro.angle())
    walter.stop()
    claw_down_coast(300, 5)
    walter.straight(-60)
    print(gyro.angle())
    attach_left_motor.run_angle(75, -10, Stop.COAST, wait=True)
    ev3.speaker.beep(500,200)
    walter.straight(-50)
    attach_left_motor.run_angle(300, 180, Stop.COAST, wait=True)
# move towards radar
    gyro_turn(-56, left_motor, right_motor, gyro, walter)
    walter.straight(460)
    gyro_turn(-34, left_motor, right_motor, gyro, walter)
# do the radar
    claw_down(350, 192)
    walter.straight(-200)
# green sample mission
    claw_up(300, 150)
    gyro_turn(55, left_motor, right_motor, gyro, walter)
    walter.straight(-75)
    stick_down_coast(700, 200)
    wait(800)
    gyro_turn(-45, left_motor, right_motor, gyro, walter)
    walter.straight(-850)
    stick_up(200, 50)