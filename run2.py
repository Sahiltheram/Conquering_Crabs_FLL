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

    walter_run_for_seconds(robot, -450, -450, 0.7)
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
    robot.walter.straight(-150)
    gyro_turn(-45, robot)
    claw_up_stalled(900, 60, robot)
    
    # we reset the angle here so that we know where we are before doing the angler fish mission,
    # so after doing it, in line 51, we can turn back to that same angle
    
    robot.gyro.reset_angle(0)
    robot.walter.straight(370)
    robot.walter.stop()
    robot.right_motor.run_angle(400, 80, Stop.HOLD, True)
    # wait(2000)
    # gyro_turn(-robot.gyro.angle(), robot)
    # wait(2000)

    # # beep to know if robot is not stalling after angler fish mission is done

    # robot.ev3.speaker.beep(500, 500)
    # wait(2000)
    # gyro_turn(8, robot)6
    # wait(2000)
    # robot.walter.straight(18)
    # wait(2000)
    # walter_run_for_seconds(robot, 0, 300, 1)
    # wait(2000)
    
    robot.ev3.speaker.beep(500, 500)

    robot.walter.straight(-50)

    # align and pick up item
    # turning back to the same angle here again, but also 65 degrees more to stay precise
    
    gyro_turn(-robot.gyro.angle(), robot)
    gyro_turn(63, robot)


    robot.walter.straight(-30)

    
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run_until_stalled(-300, Stop.COAST, 25)
    robot.walter.straight(80)
    stick_up_seconds(195, 1000, robot)
    robot.walter.straight(35)
    
    wait(100)
    
    # go back to base
    
    gyro_turn(-30, robot)
    wait(100)
    robot.walter.straight(190)
    wait(100)
    gyro_turn(-45, robot)
    wait(100)
    robot.walter.straight(200)
    wait(100)
    robot.walter.stop()
    robot.left_motor.run_angle(250, 160)
    wait(100)
    #we use two small moves instead of one big one so we can limit the speed
    robot.walter.straight(100)
    robot.walter.straight(50)
    wait(100)
    robot.walter.turn(-80) 
    # walter.stop()
    # robot.right_motor.run_angle(350, 270)
    wait(100)
    #robot.walter.settings(600, 350, 300, 115)<-- increase straight speed eventually
    robot.walter.straight(650)

    # robot.walter.straight(500)
    # robot.walter.straight(50)
    # wait(2000)
    # gyro_turn(-40, robot)
    # wait(2000)
    # robot.walter.straight(300)
    # wait(2000)
    # gyro_turn(-37.5, robot)
    # wait(2000)
    