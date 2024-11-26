from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import move_functions
from gyro_turn import *
from Container import Container




 #starting push boat
 
def run5 (robot):
    robot.walter.settings(400, 350, 200, 200)
    robot.walter.straight(180)
    robot.walter.straight(-90)
    robot.walter.stop()
    robot.right_motor.run_angle(200, 99, Stop.HOLD, wait=True)
    gyro_turn(-70, robot)
    robot.walter.straight(-100)
    robot.walter.straight(246)
    gyro_turn(92, robot)
    robot.walter.straight(327)
    gyro_turn(31, robot)
    wait(500)
    robot.attach_right_motor.run_angle(400, -120, Stop.HOLD, wait=True)
    robot.attach_right_motor.run_until_stalled(-183, Stop.HOLD, duty_limit=70)
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run_angle(50, 5, Stop.HOLD, wait=True)
    robot.walter.straight(450)
    robot.attach_right_motor.run_angle(700, 170, Stop.HOLD, wait=True)
    robot.walter.straight(-75)
    robot.walter.turn(30)
    robot.walter.straight(345)
    # gyro_turn(-90, left_motor, right_motor, gyro, walter)
    # walter.straight(-160)
    # gyro_turn(90, left_motor, right_motor, gyro, walter)
    # walter.straight(400)
    robot.walter.straight(-200)
    gyro_turn(-90, robot)
    robot.walter.straight(-80)
    robot.walter.straight(183)
    gyro_turn(90, robot)
    #Crabs
    robot.walter.straight(-20)
    robot.attach_right_motor.run_angle(400, -149, Stop.HOLD)
    robot.walter.straight(63)
    robot.attach_right_motor.run_angle(125, 130, Stop.COAST, False)
    robot.walter.straight(-192)
    robot.attach_right_motor.run_until_stalled(125, Stop.COAST, duty_limit=70)
    robot.walter.straight(-75)
    robot.attach_right_motor.run_until_stalled(130, Stop.COAST, duty_limit=70)
    robot.walter.turn(-20)
    robot.walter.straight(300)
    robot.walter.turn(20)
    robot.walter.straight(1000)