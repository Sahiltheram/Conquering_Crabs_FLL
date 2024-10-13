from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
attach_left_motor = Motor(Port.A)
attach_right_motor = Motor(Port.D)
gyro = GyroSensor(Port.S1)

def gyro_turn(angle):

    min_speed = 30
    max_speed = 1000
    threshold = 25
    speed = max_speed

    gyro.reset_angle(0)

    if (angle > 0):
        
        rem_dist = angle
           
        print("STARTING!!")

        while (rem_dist > 0): 
            
            print(rem_dist, gyro.angle(), speed)

            rem_dist = (angle - gyro.angle())

            left_motor.run(-speed)
            right_motor.run(speed)
            
            if (rem_dist < threshold):
                if (speed > min_speed):
                    speed -= ((max_speed - min_speed) / threshold)
                else:
                    speed = min_speed
            
            else:
                speed = max_speed

            if rem_dist < 5:
                break

        left_motor.hold()
        right_motor.hold()

