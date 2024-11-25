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

def gyro_turn(angle, robot):
    MAX_SPEED = 400
    MIN_SPEED = 30
    ERROR_THRESHOLD = 2
    ANGLE_FOR_MAX_SPEED = 70

    robot.gyro.reset_angle(0)
    robot.walter.stop()
    while (True):
        rem_dist = angle - robot.gyro.angle()
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
        robot.left_motor.run(speed)
        robot.right_motor.run(-speed)
        wait(15)
        if abs(rem_dist) < ERROR_THRESHOLD:
            break
    robot.left_motor.stop()
    robot.right_motor.stop()

    print("DONE, angle = " + str(robot.gyro.angle()) + " degrees")