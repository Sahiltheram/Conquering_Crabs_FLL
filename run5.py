from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import move_functions
from gyro_turn import gyro_turn
\

 #starting push boat
def run5 (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro):
    walter.straight(180)
    walter.straight(-89)
    walter.turn(-95)
    walter.straight(-55)
    walter.straight(210)
    walter.turn(91)
    walter.straight(341)
    walter.turn(42)
    walter.straight(32)
    attach_right_motor.run_angle(700, -175, Stop.COAST, wait=True)
    walter.straight(450)
    attach_right_motor.run_angle(700, 170, Stop.COAST, wait=True)
    walter.turn(-60)
    walter.straight(-150)
    walter.turn(60)
    walter.straight(400)
    wlater.straight
    #walter.turn(-130)
    #attach_left_motor.run_angle(700, 148, Stop.COAST, wait=True)
    #walter.turn(-18)
    #walter.straight(243)
    #walter.straight(50)
    #walter.turn(-125)
    #walter.straight(-123)
