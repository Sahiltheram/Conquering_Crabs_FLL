from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from move_functions import *
from gyro_turn import gyro_turn

#Coral reef area

def run3 (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro):   
     attach_left_motor.run_time(-700, 700, Stop.COAST)
     wait(1000)
     walter.straight(187)
     wait(1000)
     walter.straight(-7)
     wait(1000)
     claw_up_coast(attach_left_motor, 50, 45)
     wait(800)
     walter.straight(-50)
     claw_up(attach_left_motor, 100, 30)
     attach_left_motor.hold()
     wait(800)
     walter.turn(29)
     walter.straight(139)
     wait(500)

     claw_down(attach_left_motor, 50, 36)
     walter.turn(-30)
     claw_up_coast(attach_left_motor, 1000, 90)

     # walter.straight(60)
     # walter.straight(85)

