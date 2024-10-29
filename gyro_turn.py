from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog

def set_speed(error, threshold_test, maxspeed, minspeed):
    speed_set = (((error / threshold_test) * (maxspeed - minspeed)) + minspeed)
    return (speed_set)

def gyro_turn(angle, left_motor, right_motor, gyro):
    MAX_SPEED = 400
    MIN_SPEED = 55
    threshold = abs(angle)
    error_threshold = 2
    direction = 1
    if (angle < 0):
        direction = -1

    gyro.reset_angle(0)
    while (True): 
        rem_dist = abs(angle - gyro.angle())
        speed = max(set_speed(rem_dist, threshold, MAX_SPEED, MIN_SPEED), MIN_SPEED)
        left_motor.run(speed * direction)
        right_motor.run(-speed * direction)
        wait(20)
        #print(speed, rem_dist)
        if rem_dist < error_threshold:
            break
    left_motor.stop()
    right_motor.stop()
    print(speed, rem_dist)
