from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from gyro_turn import gyro_turn
from move_functions import *

def run2 (robot):
    # this is the commented radar backup mission
    # walter.straight(750)
    # gyro_turn(-73, left_motor, right_motor, gyro, walter)
    #get_to_sumbersible
    robot.walter.straight(545)
    gyro_turn(-55, robot)
    claw_down(500, 180, robot)
    robot.walter.straight(500)
    robot.walter.stop()
    walter_align_color(robot, 40, 40)
    walter_run_for_seconds(robot, 100, 0, 0.75)
    #do_submerible+angler_fish
    claw_up_stalled(300, 70, robot)
    claw_down(300, 30, robot)
    gyro_turn(-70, robot)
    claw_up_coast(700, 90, robot)
    robot.walter.straight(250)
    

