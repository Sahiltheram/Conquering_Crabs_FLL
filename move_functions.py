from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

def walter_run_for_seconds(right_motor, left_motor, speed, seconds):
    left_motor.run_time(speed, seconds, Stop.HOLD, False)
    right_motor.run_time(speed, seconds, Stop.HOLD, True)