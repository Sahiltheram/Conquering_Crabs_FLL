from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from move_functions import *
from gyro_turn import gyro_turn
from Container import Container



def run3_part1 (robot): 

# Coral tree
     
     robot.walter.settings(550, 400, 200, 200)  
     robot.gyro.reset_angle(0)
     robot.walter.straight(-6)
     robot.attach_left_motor.run_time(-700, 700, Stop.COAST)
     wait(500)
     robot.walter.straight(187)
     wait(200)
     robot.walter.straight(-15)
     wait(200)
     claw_up(50, 34, robot)
     wait(1000)
     robot.walter.straight(-30)
     gyro_turn(-robot.gyro.angle(), robot)
     
# Yellow handle/flower upside down 

     claw_up_stalled(400, None, robot)
     robot.walter.straight(100)
     gyro_turn(38, robot)
     robot.walter.straight(-10)
     claw_down(300, 180, robot)
     claw_down_seconds(85, 900, robot)
     robot.attach_left_motor.run_time(10, 13, Stop.BRAKE)
     walter_run_for_seconds(robot, -200, 200, 0.5)
     claw_up_coast(1000, 180, robot)

# Get ready for part 2 and align on wall
   
     robot.walter.settings(1000, 800, 200, 200)  

     gyro_turn(15, robot)
     robot.walter.straight(255)
     gyro_turn(-40, robot)
     robot.walter.straight(280)
     walter_run_for_seconds(robot, 1000, 1000, 0.8)

def run3_part2 (robot): 

# Perpare settings and angles
     
     robot.walter.settings(1000, 600, 200, 200)  
     robot.gyro.reset_angle(0)
     claw_up_seconds(300, 1.5, robot)

# Shark Mission
     
     robot.walter.straight(-170)
     gyro_turn(-46, robot)
     robot.walter.straight(-70)
     claw_down_coast(400, 170, robot)
     claw_down_seconds(100, 500, robot)
          # Unhook Claw Attachment
     robot.walter.straight(-50)
     claw_up(1000, 160, robot)
     claw_up_seconds(200, 500, robot)

# Nursery Mission
     
     gyro_turn(46, robot)
     claw_down(400, 170, robot)
     robot.walter.straight(-20)
     gyro_turn(27, robot)
     robot.walter.straight(10)
     claw_down_seconds(200, 750, robot)
     
# Go back to base

     # walter.straight(5)
     claw_up(400, 35, robot)
     robot.walter.straight(-800)