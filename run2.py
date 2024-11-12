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
    walter.straight(545)
    gyro_turn(-58, left_motor, right_motor, gyro, walter)
    walter.straight(540)
    walter.stop()
    walter_align_color(left_motor, right_motor, 40, 40, color_sensor_right, color_sensor_left)
    gyro_turn(-13, left_motor, right_motor, gyro, walter)
    walter.straight(-150)
    stick_down_coast(500, 165)
    walter.straight(50)
    stick_up_stalled(300, 0)

    

