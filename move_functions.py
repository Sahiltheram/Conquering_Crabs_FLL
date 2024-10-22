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

def claw_up(left_motor, speed, angle):
    left_motor.run_angle(speed, angle)

def claw_down(left_motor, speed, angle):
    left_motor.run_angle(speed, -angle)

def claw_up_coast(left_motor, speed, angle):
    left_motor.run_angle(speed, angle, Stop.COAST)

def claw_down_coast(left_motor, speed, angle):
    left_motor.run_angle(speed, -angle, Stop.COAST)


