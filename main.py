#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
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
from masterProgram import *
#from gyro_turn import *
#from gyro_turn import gyro_turn


# Define variables:

run_select = 5

# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
attach_left_motor = Motor(Port.A)
attach_right_motor = Motor(Port.D)
set_motors(attach_left_motor, attach_right_motor)
walter = DriveBase(left_motor, right_motor, 62.4, 98.4)
walter.settings(400, 400, 200, 200)
gyro = GyroSensor(Port.S1)
color_sensor_right = ColorSensor(Port.S2)
color_sensor_left = ColorSensor(Port.S3)

# Insert function in every run:

masterProgram(ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro, color_sensor_right, color_sensor_left)
#walter_align_color(left_motor, right_mo
# tor, 75, 75, color_sensor_right, color_sensor_left)