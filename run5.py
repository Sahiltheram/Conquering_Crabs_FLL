from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import move_functions
from gyro_turn import *


 #starting push boat
def run5 (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro):
    walter.straight(180)
    walter.straight(-89)
    walter.turn(-95)
    walter.straight(-55)
    walter.straight(215)
    gyro_turn(90, left_motor, right_motor, gyro, walter)
    walter.straight(335)
    gyro_turn(22, left_motor, right_motor, gyro, walter)
    walter.straight(20)
    attach_right_motor.run_angle(700, -175, Stop.COAST, wait=True)
    walter.straight(450)
    attach_right_motor.run_angle(700, 170, Stop.COAST, wait=True)
    walter.straight(-150)
    gyro_turn(-90, left_motor, right_motor, gyro, walter)
    walter.straight(-160)
    gyro_turn(90, left_motor, right_motor, gyro, walter)
    walter.straight(400)
    walter.straight(-200)
    gyro_turn(-90, left_motor, right_motor, gyro, walter)
    walter.straight(160)
    gyro_turn(90, left_motor, right_motor, gyro, walter)
    walter.straight(100)
    #walter.turn(-130)
    #attach_left_motor.run_angle(700, 148, Stop.COAST, wait=True)
    #walter.turn(-18)
    #walter.straight(243)
    #walter.straight(50)
    #walter.turn(-125)
    #walter.straight(-123)
