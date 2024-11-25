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

    #get to sumbersible

    robot.walter.straight(-35)
    robot.walter.straight(570)

    gyro_turn(-55, left_motor, right_motor, gyro, walter)
    claw_down(500, 170)
    robot.walter.straight(500)
    robot.walter.stop()
    walter_align_color(robot, 40, 40)
    walter_run_for_seconds(robot, 100, 0, 0.75)

    # do submerible & angler fish

    claw_up_seconds(60, 2000, robot)
    claw_down(300, 30, robot)
    gyro_turn(-10, robot)
    robot.walter.straight(-60)
    gyro_turn(-57, robot)
    claw_up(700, 90, robot)
    robot.gyro.reset_angle(0)
    
    robot.walter.straight(290)
    gyro_turn(-gyro.angle(), robot)
    robot.ev3.speaker.beep(500, 500)
    gyro_turn(8, robot)
    robot.walter.straight(18)
    walter_run_for_seconds(robot, 0, 300, 1)
    
    robot.ev3.speaker.beep(500, 500)
    wait(1000)

    robot.walter.straight(-50)

    # align and pick up item
    
    gyro_turn((-gyro.angle() + 75), robot)
    robot.walter.straight(-30)
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run_until_stalled(-300, Stop.HOLD, 25)
    robot.walter.straight(80)
    stick_up_seconds(195, 1000, robot)
    
    # move the stick down without waiting:
    # attach_right_motor.run_angle(200, -150, Stop.HOLD, False)

    # with waiting:

    # stick_down(200, 161)
    # walter.straight(130)
    # stick_up(100, 50)
    
    # #go back to base
    
    # gyro_turn(-50, left_motor, right_motor, gyro, walter)
    # walter.straight(500)
    # gyro_turn(-65, left_motor, right_motor, gyro, walter)
    # walter.straight(600)
    

