from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

def set_speed(error, threshold_test, minspeed, maxspeed):
    if (error < 0):
        speed_set = ((error / threshold_test) * maxspeed)
    else: 
        speed_set = ((error / threshold_test) * maxspeed)
    return (speed_set)

def gyro_turn(angle, left_motor, right_motor, gyro, walter):
    MAX_SPEED = 400
    MIN_SPEED = 30
    ERROR_THRESHOLD = 2
    ANGLE_FOR_MAX_SPEED = 70

    gyro.reset_angle(0)
    walter.stop()
    while (True):
        rem_dist = angle - gyro.angle()
        if rem_dist > ANGLE_FOR_MAX_SPEED:
            speed = MAX_SPEED
        elif rem_dist < -ANGLE_FOR_MAX_SPEED:
            speed = -MAX_SPEED
        else:
           speed = set_speed(rem_dist, ANGLE_FOR_MAX_SPEED, MIN_SPEED, MAX_SPEED)
           #print("error="+str(rem_dist)+", calc speed="+str(speed))
           if speed < 0:
               if abs(speed) < MIN_SPEED:
                  speed = -MIN_SPEED
               if abs(speed) > MAX_SPEED:
                  speed = -MAX_SPEED
           if (speed > 0):
               if abs(speed) < MIN_SPEED:
                  speed = MIN_SPEED
               if abs(speed) > MAX_SPEED:
                  speed = MAX_SPEED
        left_motor.run(speed)
        right_motor.run(-speed)
        wait(15)
        if abs(rem_dist) < ERROR_THRESHOLD:
            break
    left_motor.stop()
    right_motor.stop()

    print("DONE, angle = " + str(gyro.angle()) + " degrees")