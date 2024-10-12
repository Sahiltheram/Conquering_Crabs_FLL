from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

def run4 (ev3, walter, attach_left_motor, attach_right_motor):
    walter.straight(700)
    walter.turn(45)
    walter.straight(50)
    walter.straight(-50)
    walter.turn(-53)
    walter.straight(-700)