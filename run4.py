from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from gyro_turn import gyro_turn


def run4 (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro):
    walter.straight(700)
    walter.turn(45)
    walter.straight(50)
    walter.straight(-50)
    walter.turn(-53)
    walter.straight(-700)