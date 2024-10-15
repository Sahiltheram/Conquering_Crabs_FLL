from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import move_functions


 #starting push boat
def run5 (ev3, walter, attach_left_motor, attach_right_motor):
    walter.straight(225)
    walter.straight(-55)
    walter.turn(-90)
    walter.straight(110)
    walter.turn(92)
    walter.straight(300)
    attach_left_motor.run_time(700, 700, Stop.HOLD, wait=True)
