from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from move_functions import *
from gyro_turn import gyro_turn



def run3_part1 (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro): 

# Coral tree + flower upside down mission
     
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
     walter.straight(-30)
     claw_up_stalled(400, None)
     walter.straight(100)
     gyro_turn(38, left_motor, right_motor, gyro, walter)
     walter.straight(-10)
     claw_down(300, 180)
     ev3.speaker.beep(440, 100)
     wait(1000)
     claw_down_seconds(75, 1000)
     attach_left_motor.run_time(10, 10, Stop.BRAKE)
     walter_run_for_seconds(left_motor, right_motor, -200, 200, 600, walter)
     claw_up_coast(1000, 180)

# Get ready for part 2 and align on wall
   
     walter.settings(1000, 400, 200, 200)  

     gyro_turn(15, left_motor, right_motor, gyro, walter)
     walter.straight(235)
     gyro_turn(-40, left_motor, right_motor, gyro, walter)
     walter.straight(250)
     walter_run_for_seconds(left_motor, right_motor, 1000, 1000, 600, walter)

def run3_part2 (ev3, walter, left_motor, right_motor, attach_left_motor, attach_right_motor, gyro): 

# Perpare settings and angles
     
     walter.settings(1000, 400, 200, 200)  
     gyro.reset_angle(0)
     claw_up_seconds(300, 1.5)

# Shark Mission
     
     walter.straight(-180)
     gyro_turn(-45, left_motor, right_motor, gyro, walter)
     walter.straight(-70)
     claw_down_coast(400, 170)
     claw_down_seconds(100, 500)
          # Unhook Claw Attachment
     walter.straight(-50)
     claw_up(1000, 160)
     claw_up_seconds(200, 500)

# Nursery Mission
     
     gyro_turn(45, left_motor, right_motor, gyro, walter)
     claw_down(400, 170)
     walter.straight(-10)
     gyro_turn(25, left_motor, right_motor, gyro, walter)
     walter.straight(15)
     claw_down_seconds(200, 750)
     
# Go back to base

     claw_up(400, 10)
     walter.straight(-800)