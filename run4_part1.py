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
 
def run4_part1 (robot):
    robot.walter.settings(500, 350, 200, 200)
    #put samples on boat
    walter_run_for_seconds(robot, 503, 503, 1.2)
    robot.walter.straight(-90)

def BigBackBoat (robot):
    robot.walter.settings(400, 350, 200, 200)
    # #allign on wall
    walter_run_for_seconds(robot, -500, -500, 1)
    robot.walter.straight(226)
    gyro_turn(92, robot)
    robot.walter.straight(333)
    gyro_turn(18, robot)
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
    robot.walter.straight(-170)