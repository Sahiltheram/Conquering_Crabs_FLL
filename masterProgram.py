from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

from move_functions import *
from gyro_turn import gyro_turn

from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *


def masterProgram(robot):

    robot.ev3.screen.clear()
    run_select = 1
    NUMBER_OF_RUNS = 4

    missions_in_run = {
        1: "Squid",
        2: "D Arc",
        3: "Coral Tree",
        4: "Boat"}

    release_motors(True, True, True, True, robot)
    robot.ev3.screen.set_font(Font(family=None, size=100, bold=True, monospace=False, lang=None, script=None))

    while True:
        if (run_select > NUMBER_OF_RUNS):
            run_select = NUMBER_OF_RUNS
        if (run_select < 1):
            run_select = 1            

        value = missions_in_run[run_select]
        robot.ev3.screen.draw_text(80, 60, run_select, text_color=Color.BLACK, background_color=None)
        robot.ev3.screen.set_font(Font(family=None, size=30, bold=False, monospace=False, lang=None, script=None))
        robot.ev3.screen.draw_text (0, 0, (value), text_color=Color.BLACK, background_color=None)

        if (Button.LEFT in robot.ev3.buttons.pressed()):
            #wait(15)
            run_select -= 1
            robot.ev3.screen.clear()
        
        elif (Button.RIGHT in robot.ev3.buttons.pressed()):
            #wait(15)
            run_select += 1
            robot.ev3.screen.clear()
        
        elif (Button.CENTER in robot.ev3.buttons.pressed()):
            
            lock_motors(True, False, False, True, robot)
            robot.ev3.screen.clear()
            robot.ev3.speaker.beep((220 * run_select), 400)

            if run_select == 1:
                run1(robot)                
            elif run_select == 2:
                run2(robot)                
            elif run_select == 3:
                run3_part1(robot)    
                run3_part2(robot)           
            elif run_select == 4:
                run5(robot)   

            run_select += 1
            robot.ev3.screen.clear()
            
            release_motors(True, True, True, True, robot)


def release_motors (A, B, C, D, robot):
    robot.walter.stop()
    if A == True:
        robot.attach_right_motor.run_time(1, 1, Stop.COAST)
    if B == True:
        robot.right_motor.run_time(1, 1, Stop.COAST)
    if C == True:
        robot.left_motor.run_time(1, 1, Stop.COAST)
    if D == True:
        robot.attach_left_motor.run_time(1, 1, Stop.COAST)

def lock_motors (A, B, C, D, robot):
    robot.walter.stop()
    if A == True:
        robot.attach_right_motor.run_time(1, 1, Stop.HOLD)
        robot.attach_right_motor.reset_angle(0)
    if B == True:
        robot.right_motor.run_time(1, 1, Stop.HOLD)
        robot.right_motor.reset_angle(0)
    if C == True:
        robot.left_motor.run_time(1, 1, Stop.HOLD)
        robot.left_motor.reset_angle(0)
    if D == True:
        robot.attach_left_motor.run_time(1, 1, Stop.HOLD)
        robot.attach_left_motor.reset_angle(0)