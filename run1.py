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
    walter_run_for_seconds(robot, -450, -450, 0.7)
    robot.left_motor.reset_angle(0)
    robot.right_motor.reset_angle(0)
    robot.walter.straight(295)
    gyro_turn(-45, robot)
    robot.walter.straight(270)
    robot.walter.straight(-195)
    gyro_turn(92, robot)

#change_shipping_lanes

    robot.attach_left_motor.run_time(-700, 700, Stop.COAST, wait=True)

    # Print to ensure turn consistence and that the gyro is not drifting

    print(robot.gyro.angle())

    robot.walter.straight(40)
    robot.attach_left_motor.run_angle(300, 8, Stop.HOLD, True)
    robot.walter.straight(30)
    robot.attach_left_motor.run_angle(300, 25, Stop.HOLD, True)
    wait(1000)
    gyro_turn(20, robot)
    robot.walter.stop()
    claw_down_timeout(300, 5, 0.3, robot)
    robot.walter.straight(-128)
    claw_up_stalled(300, 50, robot)

# move towards radar

    gyro_turn(-56, robot)
    robot.walter.straight(503)
    gyro_turn(-29, robot)

# do the radar

    claw_down_timeout(345, 230, 1, robot)
    robot.walter.straight(-180)

# green sample mission

    claw_up(300, 150, robot)
    gyro_turn(54, robot)
    robot.walter.straight(-90)
    stick_down_timeout(350, 218, 1, robot)
    wait(300)
    walter.turn(-60)
    robot.walter.straight(-850)
    stick_up(200, 50, robot)