from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

def run3 (ev3, walter, attach_left_motor, attach_right_motor):   
     attach_left_motor.run_time(-700, 700, Stop.COAST, wait=True)
     walter.straight(185)
     wait(600)
     attach_left_motor.run_angle(125, 38, Stop.COAST, wait=True)
     wait(800)
     walter.straight(-105)
     attach_left_motor.run_time(700, 700, Stop.HOLD, wait=True)
     walter.turn(40)
     walter.straight(495)
     walter.turn(-125)
     walter.straight(70)
