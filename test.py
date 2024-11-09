from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from move_functions import *
from gyro_turn import *



def test (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro):
    attach_right_motor.run_angle(400, -180, Stop.HOLD)
    walter.straight(53)
    attach_right_motor.run_angle(125, 130, Stop.COAST, False)
    walter.straight(-183)
    attach_right_motor.run_until_stalled(125, Stop.COAST, duty_limit=70)
    wait(3000)
    walter.straight(-75)
    attach_right_motor.run_angle(125, 156, Stop.COAST)
    gyro_turn(-90, left_motor, right_motor, gyro, walter)
    walter.straight(-300)
    walter.straight(333)
    gyro_turn(90, left_motor, right_motor, gyro, walter)
    #walter.straight(1000)