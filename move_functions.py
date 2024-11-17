from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

left_motor = None
right_motor = None
timer = StopWatch()

def set_motors(left_motor1, right_motor1):
    global left_motor, right_motor
    left_motor = left_motor1
    right_motor = right_motor1

def walter_run_for_seconds(wheel_left_motor, wheel_right_motor, left_speed, right_speed, seconds, walter):
    walter.stop()
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

def stick_down_stalled(speed):
    right_motor.reset_angle(0)
    right_motor.run_until_stalled(-speed, Stop.HOLD, duty_limit = None)

def stick_up_stalled(speed):
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
        if color_sensor_left.reflection() < 15:
            wheel_left_motor.hold()
            is_stopped_left = True
        if color_sensor_right.reflection() < 15:
            wheel_right_motor.hold()
            is_stopped_right = True
        if (is_stopped_left) and (is_stopped_right):
            break


def claw_up_stalled(speed, dutylimit):    
    left_motor.reset_angle(0)
    left_motor.run_until_stalled(speed, Stop.HOLD, duty_limit = dutylimit)
    left_motor.reset_angle(0)

def claw_down_stalled(speed, dutylimit):    
    left_motor.reset_angle(0)
    left_motor.run_until_stalled(-speed, Stop.HOLD, duty_limit = dutylimit)
    left_motor.reset_angle(0)

def claw_down_seconds(speed, seconds):
    left_motor.run_time(-speed, seconds)
    left_motor.reset_angle(0)

def claw_up_seconds(speed, seconds):
    left_motor.run_time(speed, seconds)
    left_motor.reset_angle(0)

def stick_down_seconds(speed, seconds):
    right_motor.run_time(-speed, seconds)
    right_motor.reset_angle(0)

def stick_up_seconds(speed, seconds):
    right_motor_motor.run_time(speed, seconds)
    right_motor_motor.reset_angle(0)

def claw_down_timeout(speed, angle, timeout_seconds):
    timeout_ms = timeout_seconds * 1000
    left_motor.reset_angle(0)
    left_motor.run(-speed)
    timer.reset()
    while True:
        if (left_motor.angle() < -angle) or (timer.time() > timeout_ms):
            break
    left_motor.hold()

def claw_up_timeout(speed, angle, timeout_seconds):
    timeout_ms = timeout_seconds * 1000
    left_motor.reset_angle(0)
    left_motor.run(speed)
    timer.reset()
    while True:
        if (left_motor.angle() > angle) or (timer.time() > timeout_ms):
            break
    left_motor.hold()

def stick_down_timeout(speed, angle, timeout_seconds):
    timeout_ms = timeout_seconds * 1000
    right_motor.reset_angle(0)
    right_motor.run(-speed)
    timer.reset()
    while True:
        if (right_motor.angle() < -angle) or (timer.time() > timeout_ms):
            break
    right_motor.hold()
    
def stick_up_timeout(speed, angle, timeout_seconds):
    timeout_ms = timeout_seconds * 1000
    right_motor.reset_angle(0)
    right_motor.run(speed)
    timer.reset()
    while True:
        if (right_motor.angle() > angle) or (timer.time() > timeout_ms):
            break
    right_motor.hold()



