from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from move_functions import *

from gyro_turn import gyro_turn



def run1 (robot):
#unexpected encounter
    robot.walter.settings(600, 350, 300, 115)
    robot.left_motor.reset_angle(0)
    robot.right_motor.reset_angle(0)
    robot.walter.straight(295)
    gyro_turn(-45, robot)
    robot.walter.straight(270)
    robot.walter.straight(-165)
    gyro_turn(92, robot)
#change_shipping_lanes
    robot.attach_left_motor.run_time(-700, 700, Stop.COAST, wait=True)
    print(robot.gyro.angle())
    robot.walter.straight(57)
    robot.attach_left_motor.run_angle(300, 8, Stop.HOLD, True)
    robot.walter.straight(18)
    robot.attach_left_motor.run_angle(300, 30, Stop.HOLD, True)
    wait(1000)
    print(robot.gyro.angle())
    gyro_turn(20, robot)
    print(robot.gyro.angle())
    robot.walter.stop()
    claw_down_coast(300, 5, robot)
    robot.walter.straight(-60)
    print(robot.gyro.angle())
    robot.attach_left_motor.run_angle(75, -10, Stop.COAST, wait=True)
    robot.ev3.speaker.beep(500,200)
    robot.walter.straight(-50)
    robot.attach_left_motor.run_angle(300, 180, Stop.COAST, wait=True)
# move towards radar
    gyro_turn(-56, robot)
    robot.walter.straight(460)
    gyro_turn(-34, robot)
# do the radar
    claw_down(350, 192, robot)
    robot.walter.straight(-200)
# green sample mission
    claw_up(300, 150, robot)
    gyro_turn(55, robot)
    robot.walter.straight(-75)
    stick_down_coast(700, 200, robot)
    wait(800)
    gyro_turn(-45, robot)
    robot.walter.straight(-850)
    stick_up(200, 50, robot)