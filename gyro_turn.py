from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

def set_speed(error, threshold_test, maxspeed, minspeed):
    if (error < 0):
        speed_set = (((error / threshold_test) * (maxspeed - minspeed)) - minspeed)
    else: 
        speed_set = (((error / threshold_test) * (maxspeed - minspeed)) + minspeed)
    return (speed_set)

def gyro_turn(angle, left_motor, right_motor, gyro, walter):
    MAX_SPEED = 300
    MIN_SPEED = 30
    error_threshold = 2
    angle_for_max_speed = 40
    gyro.reset_angle(0)
    walter.stop()
    while (True): 
        rem_dist = angle - gyro.angle()
        if (abs(rem_dist) > angle_for_max_speed):
            speed = MAX_SPEED
        else: 
            speed = set_speed(rem_dist, angle, MAX_SPEED, MIN_SPEED)
            left_motor.run(speed)
            right_motor.run(-speed)
            wait(15)
        #print(speed, rem_dist)
        if abs(rem_dist) < error_threshold:
            break
    left_motor.stop()
    right_motor.stop()
    print(speed, rem_dist)
