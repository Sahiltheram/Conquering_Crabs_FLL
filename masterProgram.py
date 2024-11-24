from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

from move_functions import *

from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *
from run5test import *
from gyro_turn import gyro_turn


def masterProgram(ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro, color_sensor_right, color_sensor_left):

    ev3.screen.clear()
    run_select = 1
    NUMBER_OF_RUNS = 4

    missions_in_run = {
        1: "Squid",
        2: "D Arc",
        3: "Coral Tree",
        4: "Boat"}

    release_motors(True, True, True, True, attach_left_motor, attach_right_motor, left_motor, right_motor, walter)
    ev3.screen.set_font(Font(family=None, size=100, bold=True, monospace=False, lang=None, script=None))

    while True:
        value = missions_in_run[run_select]
        ev3.screen.draw_text(80, 60, run_select, text_color=Color.BLACK, background_color=None)
        ev3.screen.set_font(Font(family=None, size=30, bold=False, monospace=False, lang=None, script=None))
        ev3.screen.draw_text (0, 0, (value), text_color=Color.BLACK, background_color=None)

        if (run_select > NUMBER_OF_RUNS):
            run_select = NUMBER_OF_RUNS

        if (run_select < 1):
            run_select = 1

        if (Button.LEFT in ev3.buttons.pressed()):
            while (Button.LEFT in ev3.buttons.pressed()):
                wait(10)
            run_select -= 1
            ev3.screen.clear()
        
        elif (Button.RIGHT in ev3.buttons.pressed()):
            while (Button.RIGHT in ev3.buttons.pressed()):
                wait(10)
            run_select += 1
            ev3.screen.clear()
        
        elif (Button.CENTER in ev3.buttons.pressed()):
            
            lock_motors(True, False, False, True, left_motor, right_motor, attach_left_motor, attach_right_motor, walter)
            ev3.screen.clear()
            ev3.speaker.beep((220 * run_select), 400)

            if run_select == 1:
                run1(ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro)                
            elif run_select == 2:
                run2(ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro, color_sensor_right, color_sensor_left)                
            elif run_select == 3:
                run3_part1(ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro)    
                run3_part2(ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro)           
            elif run_select == 4:
                run5test(ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro)   

            run_select += 1
            ev3.screen.clear()
            
            release_motors(True, True, True, True, attach_left_motor, attach_right_motor, left_motor, right_motor, walter)


def release_motors (A, B, C, D, attach_left_motor, attach_right_motor, left_motor, right_motor, walter):
    walter.stop()
    if A == True:
        attach_right_motor.run_time(1, 1, Stop.COAST)
    if B == True:
        right_motor.run_time(1, 1, Stop.COAST)
    if C == True:
        left_motor.run_time(1, 1, Stop.COAST)
    if D == True:
        attach_left_motor.run_time(1, 1, Stop.COAST)

def lock_motors (A, B, C, D, attach_left_motor, attach_right_motor, left_motor, right_motor, walter):
    walter.stop()
    if A == True:
        attach_right_motor.run_time(1, 1, Stop.HOLD)
        attach_right_motor.reset_angle(0)
    if B == True:
        right_motor.run_time(1, 1, Stop.HOLD)
        right_motor.reset_angle(0)
    if C == True:
        left_motor.run_time(1, 1, Stop.HOLD)
        ledt_motor.reset_angle(0)
    if D == True:
        attach_left_motor.run_time(1, 1, Stop.HOLD)
        attach_left_motor.reset_angle(0)