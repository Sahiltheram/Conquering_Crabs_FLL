import sys
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import os

# Define the file path
file_path = '/home/robot/color.txt'

def scale_color_value(color_white, color_black, color_org_val):

    mini = color_black
    maxi = color_white

    value = (((float(color_org_val) - float(mini)) / (float(maxi) - float(mini))) * 100)

    return(value)

def calibrate_color(robot):
    
    center_pressed = False

    robot.ev3.screen.draw_text(20, 60, "Place on Black", text_color=Color.BLACK, background_color=None)
    
    while not center_pressed:
        center_pressed = (Button.CENTER in robot.ev3.buttons.pressed())

    value_on_black_left = robot.color_sensor_left.reflection()
    value_on_black_right = robot.color_sensor_right.reflection()
    value_on_black = ((value_on_black_left + value_on_black_right) / 2)

    center_pressed = False

    robot.ev3.screen.clear()
    robot.ev3.screen.draw_text(20, 60, "Place on White", text_color=Color.BLACK, background_color=None)
    
    wait(1000)

    while not center_pressed:
        center_pressed = (Button.CENTER in robot.ev3.buttons.pressed())

    value_on_white_left = robot.color_sensor_left.reflection()
    value_on_white_right = robot.color_sensor_right.reflection()
    value_on_white = ((value_on_white_left + value_on_white_right) / 2)

    print(value_on_white, value_on_black)

    try: 

        # Open the file in write mode ('w')
        color_file = open(file_path, 'w')
        # Write a number to the file
        color_file.write(str(value_on_white) + " " + str(value_on_black))
        color_file.close()

    except:

        print("error")

def fetch_calibrated_color(color_sens_select, robot):

    robot.ev3.light.on(Color.GREEN)

    if color_sens_select == 'LEFT':
        color_org_val = robot.color_sensor_left.reflection()
    elif color_sens_select == 'RIGHT':
        color_org_val = robot.color_sensor_right.reflection()

    return(scale_color_value(robot.color_white, robot.color_black, color_org_val))