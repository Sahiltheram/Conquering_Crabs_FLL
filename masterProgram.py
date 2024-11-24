from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from move_functions import *

from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *
from run5test import *
from gyro_turn import gyro_turn


def masterProgram(ev3):

    ev3.screen.clear()
    run_select = 1

    release_motors(True, True, True, True)

    while True:
        
        ev3.screen.draw_text(0, 0, run_select, text_color=Color.BLACK, background_color=None)

        if (Button.LEFT in ev3.buttons.pressed()) and (run_select > 0):
            while (Button.LEFT in ev3.buttons.pressed()):
                wait(10)
            run_select -= 1
            ev3.screen.clear()
        
        elif (Button.RIGHT in ev3.buttons.pressed()) and (run_select < 5):
            while (Button.RIGHT in ev3.buttons.pressed()):
                wait(10)
            run_select += 1
            ev3.screen.clear()
        
        elif (Button.CENTER in ev3.buttons.pressed()):
            
            lock_motors(True, False, False, True)
            ev3.screen.clear()
            ev3.speaker.beep((220 * run_select), 400)

            if run_select == 1:
                pass
                #run1(...)                
            elif run_select == 2:
                pass
                #run2(...)                
            elif run_select == 3:
                pass                
                #run3(...)                
            elif run_select == 4:
                pass
                #run4(...)                
                
            if run_select < 4:
                run_select += 1
            
            release_motors(True, True, True, True)


def release_motors (A, B, C, D):
    if A ==True:
        attach_right_motor.run_time(1, 1, Stop.COAST)
    if B == True:
        right_motor.run_time(1, 1, Stop.COAST)
    if C == True:
        left_motor.run_time(1, 1, Stop.COAST)
    if D == True:
        attach_left_motor.run_time(1, 1, Stop.COAST)

def lock_motors (A, B, C, D):
    if A == True:
        attach_right_motor.run_time(1, 1, Stop.HOLD)
    if B == True:
        right_motor.run_time(1, 1, Stop.HOLD)
    if C == True:
        left_motor.run_time(1, 1, Stop.HOLD)
    if D == True:
        attach_left_motor.run_time(1, 1, Stop.HOLD)