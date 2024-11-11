from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from move_functions import *
from gyro_turn import gyro_turn

#Coral tree area

def run3 (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro): 
     walter.settings(400, 350, 200, 200)  
     attach_left_motor.run_time(-700, 700, Stop.COAST)
     wait(1000)
     walter.straight(187)
     wait(1000)
     walter.straight(-23)
     wait(1000)
     claw_up(50, 30)
     wait(800)
     claw_up_coast(20, 10)
     wait(800)
     walter.straight(-50)
     claw_up(100, 30)
     wait(5000)
     ev3.speaker.beep(4000, 500)
     walter.turn(29)
     walter.straight(139)
     wait(500)
     claw_down(50, 36)
     walter.turn(-30)
     claw_up_coast(1000, 90)
     walter.turn(32)


     # walter.straight(60)
     # walter.straight(85)