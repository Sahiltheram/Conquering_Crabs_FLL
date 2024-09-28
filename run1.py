from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



def run1 (ev3, walter, attach_left_motor, attach_right_motor, right_motor, left_motor, walter_run_for_seconds):
    walter.straight(315)
    walter.turn(-45)
    walter.straight(220)
    #walter_run_for_seconds(100, 1)
    walter.straight(-20)
    walter.turn(70)