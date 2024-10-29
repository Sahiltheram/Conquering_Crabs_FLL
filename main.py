#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from move_functions import *

from run1 import run1
from run2 import run2
from run3 import run3
from run4 import run4
from run5 import run5
from test import test
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
walter = DriveBase(left_motor, right_motor, 62.4, 98.4)
walter.settings(400, 200, 200, 75)
gyro = GyroSensor(Port.S1)

# Insert function in every run:

run3(ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro)


