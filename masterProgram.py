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

# combines all missions and runs into one program so that it
# is easier and saves us time to start runs.
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

        # make sure the run number is valid
        # we have to ensure validity before checking the buttons so run_number does not exceed boundaries

        if (run_select > NUMBER_OF_RUNS):
            run_select = NUMBER_OF_RUNS
        if (run_select < 1):
            run_select = 1  

        # display run name and number on the screen
        value = missions_in_run[run_select]
        robot.ev3.screen.draw_text(80, 60, run_select, text_color=Color.BLACK, background_color=None)
        robot.ev3.screen.set_font(Font(family=None, size=30, bold=False, monospace=False, lang=None, script=None))
        robot.ev3.screen.draw_text(0, 0, (value), text_color=Color.BLACK, background_color=None)

    # Check which buttons are pressed

        center_pressed = False
        right_pressed = False
        left_pressed = False
        anything_pressed = False

        # green light to show that robot is ready -> you can now change/start the run

        robot.ev3.light.on(Color.GREEN)

    # This 'while loop' is updating the variables to see if a button is pressed until it is pressed. The reason we have this 
    # is because we ran into a problem where, when we checked it in the 'if' statements, a button had to be pressed before it 
    # was checked, giving us a very little window of time as Python runs fast. So we solved this by giving us infinite time,
    # but when a button is pressed, the loop breaks. 

        while not anything_pressed:

            center_pressed = (Button.CENTER in robot.ev3.buttons.pressed())
            right_pressed = (Button.RIGHT in robot.ev3.buttons.pressed())
            left_pressed = (Button.LEFT in robot.ev3.buttons.pressed())
        
            anything_pressed = center_pressed or right_pressed or left_pressed

        robot.ev3.light.on(Color.YELLOW)          

        # left button reduces run
        if left_pressed:
            #wait(15)
            run_select -= 1
            robot.ev3.screen.clear()
        
        # right button increases run
        elif right_pressed:
            #wait(15)
            run_select += 1
            robot.ev3.screen.clear()
        
        # center button runs the run
        elif center_pressed:
            
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
            
            # Release motors so we can move the attachments
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