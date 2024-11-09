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
    walter.straight(-90)
    walter.stop()
    right_motor.run_angle(200, 50, Stop.HOLD, wait=True)
    walter.turn(-95)
    walter.straight(-55)
    walter.straight(246)
    gyro_turn(90, left_motor, right_motor, gyro, walter)
    walter.straight(300)
    gyro_turn(32.5, left_motor, right_motor, gyro, walter)
    wait(500)
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
    walter.straight(-80)
    walter.straight(178)
    gyro_turn(90, left_motor, right_motor, gyro, walter)
    #Crabs
    walter.straight(-20)
    attach_right_motor.run_angle(400, -180, Stop.HOLD)
    walter.straight(53)
    attach_right_motor.run_angle(125, 130, Stop.COAST, False)
    walter.straight(-192)
    attach_right_motor.run_until_stalled(125, Stop.COAST, duty_limit=70)
    walter.straight(-75)
    attach_right_motor.run_angle(400, 156, Stop.COAST)
    walter.turn(-20)
    walter.straight(300)
    walter.turn(20)
    walter.straight(1000)
