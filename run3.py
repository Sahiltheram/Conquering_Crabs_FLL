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
     gyro.reset_angle(0)
     attach_left_motor.run_time(-700, 700, Stop.COAST)
     wait(1000)
     walter.straight(187)
     wait(1000)
     walter.straight(-15)
     wait(1000)
     claw_up(50, 35)
     gyro_turn(-gyro.angle(), left_motor, right_motor, gyro, walter)
     wait(800)
     walter.straight(-50)
     claw_up_stalled(400)
     gyro_turn(28, left_motor, right_motor, gyro, walter)
     wait(1000)
     walter.straight(140)
     claw_down(260, 225)
     gyro_turn(-10, left_motor, right_motor, gyro, walter)
     wait(1000)
     claw_up_stalled(400)
     gyro_turn(17, left_motor, right_motor, gyro, walter)
     walter.straight(235)
     gyro_turn(-35, left_motor, right_motor, gyro, walter)
     walter.straight(300)
     walter.straight(80)
     walter.straight(-230)
     gyro_turn(-45, left_motor, right_motor, gyro, walter)
     claw_down(150, 220)
     walter.straight(-200)