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
    # the commented radar backup mission:

    # walter.straight(750)
    # gyro_turn(-73, left_motor, right_motor, gyro, walter)

    # we have to set settings at the beginning of every run
    
    robot.walter.settings(600, 350, 300, 115)

    # get to sumbersible

    robot.walter.straight(-35)
    robot.walter.straight(570)
    gyro_turn(-55, robot)
    claw_down(500, 170, robot)
    robot.walter.straight(500)
    robot.walter.stop()
    
    # the align color is to align on the line and get to the same angle
    # the run for seconds does a one-wheel turn to anign on the submersible mission and get attachment to the right place

    walter_align_color(robot, 40, 40)
    walter_run_for_seconds(robot, 100, 0, 0.75)

# do submerible & angler fish

    claw_up_seconds(60, 2000, robot)
    claw_down(300, 30, robot)
    gyro_turn(-10, robot)
    robot.walter.straight(-60)
    gyro_turn(-53, robot)
    claw_up(700, 90, robot)
    
    # we reset the angle here so that we know where we are before doing the angler fish mission,
    # so after doing it, in line 51, we can turn back to that same angle
    
    robot.gyro.reset_angle(0)
    robot.walter.straight(290)
    gyro_turn(-robot.gyro.angle(), robot)

    # beep to know if robot is not stalling after angler fish mission is done

    robot.ev3.speaker.beep(500, 500)
    gyro_turn(8, robot)
    robot.walter.straight(18)
    walter_run_for_seconds(robot, 0, 300, 1)
    
    robot.ev3.speaker.beep(500, 500)
    wait(1000)

    robot.walter.straight(-50)

    # align and pick up item
    # turning back to the same angle here again, but also 65 degrees more to stay precise
    
    gyro_turn((-robot.gyro.angle() + 65), robot)
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
    
    # go back to base
    
    wait(3000)
    gyro_turn(-65.4321, robot)
    wait(1000)
    robot.walter.straight(500)
    wait(1000)
    gyro_turn(-60, robot)
    wait(1000)
    robot.walter.straight(600)