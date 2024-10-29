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
    walter.straight(-89)
    walter.turn(-95)
    walter.straight(210)
    walter.turn(86)
    walter.straight(487.654321)
    walter.turn(144)
    attach_left_motor.run_angle(700, -148, Stop.COAST, wait=True)
    walter.turn(-111)
    attach_left_motor.run_angle(700, 148, Stop.COAST, wait=True)
