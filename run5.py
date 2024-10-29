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
    walter.straight(180)
    walter.straight(-89)
    walter.turn(-95)
    walter.straight(-55)
    walter.straight(210)
    walter.turn(91)
    walter.straight(341)
    walter.turn(47)
    walter.straight(28)
    claw_down(left_motor, 700, -168)
    #attach_right_motor.run_angle(700, -168, Stop.COAST, wait=True)
    walter.straight(450)
    attach_right_motor.run_angle(700, 170, Stop.COAST, wait=True)
    walter.straight(-30)
    walter.turn(35)
    walter.straight(100)
    #walter.turn(-130)
    #attach_left_motor.run_angle(700, 148, Stop.COAST, wait=True)
    #walter.turn(-18)
    #walter.straight(243)
    #walter.straight(50)
    #walter.turn(-125)
    #walter.straight(-123)
