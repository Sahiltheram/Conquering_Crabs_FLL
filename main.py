#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from run1 import run1
from run2 import run2


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
attach_left_motor = Motor(Port.A)
attach_right_motor = Motor(Port.D)
walter = DriveBase(left_motor, right_motor, 62.4, 98.4)
walter.settings(400, 200, 200, 75)

# Insert function in every run:
def walter_run_for_seconds(speed, seconds):
    left_motor.run_time(speed, seconds, Stop.HOLD, False)
    right_motor.run_time(speed, seconds, Stop.HOLD, True)


run1(ev3, walter, attach_left_motor, attach_right_motor, right_motor, left_motor, walter_run_for_seconds)

