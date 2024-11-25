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
 
def run5test (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro):
    walter.settings(400, 350, 200, 200)
    walter.straight(180)
    walter.straight(-90)
    walter.stop()
    right_motor.run_angle(200, 99, Stop.HOLD, wait=True)
    gyro_turn(-70, left_motor, right_motor, gyro, walter)
    walter.straight(-100)
    walter.straight(246)
    gyro_turn(92, left_motor, right_motor, gyro, walter)
    walter.straight(327)
    gyro_turn(31, left_motor, right_motor, gyro, walter)
    wait(500)
    attach_right_motor.run_angle(400, -120, Stop.HOLD, wait=True)
    attach_right_motor.run_until_stalled(-183, Stop.HOLD, duty_limit=70)
    attach_right_motor.reset_angle(0)
    attach_right_motor.run_angle(50, 5, Stop.HOLD, wait=True)
    walter.straight(450)
    attach_right_motor.run_angle(700, 170, Stop.HOLD, wait=True)
    walter.straight(-75)
    walter.turn(30)
    walter.straight(345)
    # gyro_turn(-90, left_motor, right_motor, gyro, walter)
    # walter.straight(-160)
    # gyro_turn(90, left_motor, right_motor, gyro, walter)
    # walter.straight(400)
    walter.straight(-200)
    gyro_turn(-90, left_motor, right_motor, gyro, walter)
    walter.straight(-80)
    walter.straight(183)
    gyro_turn(90, left_motor, right_motor, gyro, walter)
    #Crabs
    walter.straight(-20)
    attach_right_motor.run_angle(400, -149, Stop.HOLD)
    walter.straight(63)
    attach_right_motor.run_angle(125, 130, Stop.COAST, False)
    walter.straight(-192)
    attach_right_motor.run_until_stalled(125, Stop.COAST, duty_limit=70)
    walter.straight(-75)
    attach_right_motor.run_until_stalled(130, Stop.COAST, duty_limit=70)
    walter.turn(-20)
    walter.straight(300)
    walter.turn(20)
    walter.straight(1000)