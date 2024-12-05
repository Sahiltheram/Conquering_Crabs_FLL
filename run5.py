from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from move_functions import *
from gyro_turn import *
from Container import Container




 #starting push boat
 
def run5 (robot):
    robot.walter.settings(400, 350, 200, 200)
    #put samples on boat
    robot.walter.straight(210)
    robot.walter.straight(-90)
    robot.walter.stop()
    gyro_turn(-93, robot)
    #allign on wall
    walter_run_for_seconds(robot, -500, -500, 1)
    robot.walter.straight(246)
    gyro_turn(92, robot)
    robot.walter.straight(353)
    gyro_turn(25, robot)
    wait(500)
    robot.walter.straight(-15)
    #hit boat most of the way
    stick_down(400, 120, robot)
    #hit boat the rest of the way
    stick_down_timeout(183, 70, 0.8, robot)
    robot.attach_right_motor.reset_angle(0)
    stick_up(50, 5, robot)
    #push the boat half way
    robot.walter.straight(460)
    stick_up(700,170, robot)
    #adjust placement to push the boat from behind
    robot.walter.straight(-75)
    robot.walter.turn(30)
    robot.walter.straight(370)
    walter_run_for_seconds(robot, -500, -500, 1)
    #allign on wall
    gyro_turn(-90, robot)
    robot.walter.straight(-80)
    #set up for crab tower
    robot.walter.straight(183)
    gyro_turn(90, robot)
    #Crabs
    robot.walter.straight(-20)
    stick_down(400, -149, robot)
    robot.walter.straight(63)
    #raise tower
    robot.attach_right_motor.run_angle(125, 130, Stop.COAST, False)
    robot.walter.straight(-192)
    robot.attach_right_motor.run_until_stalled(125, Stop.COAST, duty_limit=70)
    robot.walter.straight(-75)
    robot.attach_right_motor.run_until_stalled(130, Stop.COAST, duty_limit=70)
    #go to right home area
    robot.walter.turn(-20)
    robot.walter.straight(300)
    robot.walter.turn(20)
    robot.walter.straight(1000)