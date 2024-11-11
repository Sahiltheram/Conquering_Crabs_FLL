from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from gyro_turn import gyro_turn
from move_functions import *

def run2 (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro, color_sensor_right, color_sensor_left):
    # this is the commented radar backup mission
    # walter.straight(750)
    # gyro_turn(-73, left_motor, right_motor, gyro, walter)
    walter.straight(550)
    gyro_turn(-63, left_motor, right_motor, gyro, walter)
    walter.straight(520)
    walter.stop()
    walter_align_color(left_motor, right_motor, 75, 75, color_sensor_right, color_sensor_left)

