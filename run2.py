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
    #get_to_sumbersible
    walter.straight(545)
    gyro_turn(-55, left_motor, right_motor, gyro, walter)
    claw_down(500, 180)
    walter.straight(500)
    walter.stop()
    walter_align_color(left_motor, right_motor, 40, 40, color_sensor_right, color_sensor_left)
    walter_run_for_seconds(left_motor, right_motor, 100, 0, 0.75, walter)
    #do_submerible+angler_fish
    claw_up_stalled(300,70)
    claw_down(300, 30)
    gyro_turn(-70, left_motor, right_motor, gyro, walter)
    claw_up_coast(700, 90)
    walter.straight(250)
    

