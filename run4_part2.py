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

 #align on wall for crabs
def run4_part2 (robot):
    gyro_turn(-90, robot)
    # #crabs
    robot.walter.straight(-49)
    # wait(2000)
    # stick_down_timeout(250, 190, 1, robot)
    # wait(1000)
    # stick_up(250, 7.5, robot)
    # robot.walter.straight(63)
    # wait(2000)
    # robot.attach_right_motor.run_angle(125, 130, Stop.COAST, False)
    # wait(2000)
    # robot.walter.straight(-192)
    # wait(2000)
    # robot.attach_right_motor.run_until_stalled(125, Stop.COAST, duty_limit=70)
    # wait(2000)
    # robot.walter.straight(-75)
    # wait(2000)
    # robot.attach_right_motor.run_until_stalled(130, Stop.COAST, duty_limit=70)
    # wait(2000)
    # robot.walter.turn(-20)
    # robot.walter.straight(300)
    # robot.walter.turn(20)
    # robot.walter.straight(1000)