from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

left_motor = None
right_motor = None

def set_motors(left_motor1, right_motor1):
    global left_motor, right_motor
    left_motor = left_motor1
    right_motor = right_motor1

def walter_run_for_seconds(wheel_left_motor, wheel_right_motor, left_speed, right_speed, seconds):
    wheel_left_motor.run_time(left_speed, seconds, Stop.HOLD, False)
    wheel_right_motor.run_time(right_speed, seconds, Stop.HOLD, True)

def claw_up(speed, angle):
    left_motor.reset_angle(0)
    left_motor.run_angle(speed, angle)

def claw_down(speed, angle):
    left_motor.reset_angle(0)
    left_motor.run_angle(speed, -angle)

def claw_up_coast(speed, angle):
    left_motor.reset_angle(0)
    left_motor.run_angle(speed, angle, Stop.COAST)

def claw_down_coast(speed, angle):
    left_motor.reset_angle(0)
    left_motor.run_angle(speed, -angle, Stop.COAST)

def stick_up(speed, angle):
    right_motor.reset_angle(0)
    right_motor.run_angle(speed, angle)

def stick_down(speed, angle):
    right_motor.reset_angle(0)
    right_motor.run_angle(speed, -angle)

def stick_up_coast(speed, angle):
    right_motor.reset_angle(0)
    right_motor.run_angle(speed, angle, Stop.COAST)

def stick_down_coast(speed, angle):
    right_motor.reset_angle(0)
    right_motor.run_angle(speed, -angle, Stop.COAST)

def stick_down_stalled(speed, angle):
    right_motor.reset_angle(0)
    right_motor.run_until_stalled(-speed, Stop.HOLD, duty_limit = None)

def stick_up_stalled(speed, angle):
    right_motor.reset_angle(0)
    right_motor.run_until_stalled(speed, Stop.HOLD, duty_limit = None)

def walter_align_color(wheel_left_motor, wheel_right_motor, left_speed, right_speed, color_sensor_right, color_sensor_left):
    wheel_left_motor.run(left_speed)
    wheel_right_motor.run(right_speed)
    
    is_stopped_left = False
    is_stopped_right = False
    
    while True:
        if color_sensor_left.reflection() > 50:
            wheel_left_motor.hold()
            is_stopped_left = True
        if color_sensor_right.reflection() > 50:
            wheel_right_motor.hold()
            is_stopped_right = True
        if (is_stopped_left) and (is_stopped_right):
            break
    wheel_left_motor.run(left_speed)
    wheel_right_motor.run(right_speed)
    
    is_stopped_left = False
    is_stopped_right = False
    
    while True:
        if color_sensor_left.reflection() < 10:
            wheel_left_motor.hold()
            is_stopped_left = True
        if color_sensor_right.reflection() < 10:
            wheel_right_motor.hold()
            is_stopped_right = True
        if (is_stopped_left) and (is_stopped_right):
            break




