from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from CalibrateColorSensor import *

timer = StopWatch()
#this is used to allign on walls, mission, and for moving one motor for seconds
def walter_run_for_seconds(robot, left_speed, right_speed, seconds):
    robot.walter.stop()
    robot.left_motor.run_time(left_speed, seconds * 1000, Stop.HOLD, False)
    robot.right_motor.run_time(right_speed, seconds * 1000, Stop.HOLD, True)
#use for moving claw up and down
def claw_up(speed, angle, robot):
    robot.attach_left_motor.reset_angle(0)
    robot.attach_left_motor.run_angle(speed, angle)

def claw_down(speed, angle, robot):
    robot.attach_left_motor.reset_angle(0)
    wait(50)
    robot.attach_left_motor.run_angle(speed, -angle)

#use for moving the claw up and down while keeping it in coast
def claw_up_coast(speed, angle, robot):
    robot.attach_left_motor.reset_angle(0)
    robot.attach_left_motor.run_angle(speed, angle, Stop.COAST)

def claw_down_coast(speed, angle, robot):
    robot.attach_left_motor.reset_angle(0)
    robot.attach_left_motor.run_angle(speed, -angle, Stop.COAST)

#use for moving the stick up and down
def stick_up(speed, angle, robot):
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run_angle(speed, angle)

def stick_down(speed, angle, robot):
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run_angle(speed, -angle)

#use for moving stick up and down in coast
def stick_up_coast(speed, angle, robot):
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run_angle(speed, angle, Stop.COAST)

def stick_down_coast(speed, angle, robot):
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run_angle(speed, -angle, Stop.COAST)

#use for resetting the stick
def stick_down_stalled(speed, dutylimit, robot):
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run_until_stalled(-speed, Stop.HOLD, duty_limit = dutylimit)

def stick_up_stalled(speed, dutylimit, robot):
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run_until_stalled(speed, Stop.HOLD, duty_limit = dutylimit)

#use for color alligning(on white)
def walter_align_color(robot, left_speed, right_speed):
    robot.left_motor.run(left_speed)
    robot.right_motor.run(right_speed)
    
    is_stopped_left = False
    is_stopped_right = False
    
    while True:
        if fetch_calibrated_color("LEFT", robot) > 80:
            robot.left_motor.hold()
            is_stopped_left = True
        if fetch_calibrated_color("RIGHT", robot) > 80:
            robot.right_motor.hold()
            is_stopped_right = True
        if (is_stopped_left) and (is_stopped_right):
            break

#use for resetting claw
def claw_up_stalled(speed, dutylimit, robot):    
    robot.attach_left_motor.reset_angle(0)
    robot.attach_left_motor.run_until_stalled(speed, Stop.HOLD, duty_limit = dutylimit)
    robot.attach_left_motor.reset_angle(0)


def claw_down_stalled(speed, dutylimit, robot):    
    robot.attach_left_motor.reset_angle(0)
    robot.attach_left_motor.run_until_stalled(-speed, Stop.HOLD, duty_limit = dutylimit)
    robot.attach_left_motor.reset_angle(0)

#use for moving claw when you dont need to be as accurate
def claw_down_seconds(speed, seconds, robot):
    robot.attach_left_motor.run_time(-speed, seconds)
    robot.attach_left_motor.reset_angle(0)

def claw_up_seconds(speed, seconds, robot):
    robot.attach_left_motor.run_time(speed, seconds)
    robot.attach_left_motor.reset_angle(0)

#use for moving stick when you dont need to be as accurate
def stick_down_seconds(speed, seconds, robot):
    robot.attach_right_motor.run_time(-speed, seconds)
    robot.attach_right_motor.reset_angle(0)

def stick_up_seconds(speed, seconds, robot):
    robot.attach_right_motor.run_time(speed, seconds)
    robot.attach_right_motor.reset_angle(0)

#use for moving claw up and down when it might get stuck
def claw_down_timeout(speed, angle, timeout_seconds, robot):
    timeout_ms = timeout_seconds * 1000
    robot.attach_left_motor.reset_angle(0)
    robot.attach_left_motor.run(-speed)
    timer.reset()
    while True:
        if (robot.attach_left_motor.angle() < -angle) or (timer.time() > timeout_ms):
            break
    robot.attach_left_motor.hold()

def claw_up_timeout(speed, angle, timeout_seconds, robot):
    timeout_ms = timeout_seconds * 1000
    robot.attach_left_motor.reset_angle(0)
    robot.attach_left_motor.run(speed)
    timer.reset()
    while True:
        if (robot.attach_left_motor.angle() > angle) or (timer.time() > timeout_ms):
            break
    robot.attach_left_motor.hold()

#use for moving stick up and down when it might get stuck
def stick_down_timeout(speed, angle, timeout_seconds, robot):
    timeout_ms = timeout_seconds * 1000
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run(-speed)
    timer.reset()
    while True:
        if (robot.attach_right_motor.angle() < -angle) or (timer.time() > timeout_ms):
            break
    robot.attach_right_motor.hold()
    
def stick_up_timeout(speed, angle, timeout_seconds, robot):
    timeout_ms = timeout_seconds * 1000
    robot.attach_right_motor.reset_angle(0)
    robot.attach_right_motor.run(speed)
    timer.reset()
    while True:
        if (robot.attach_right_motor.angle() > angle) or (timer.time() > timeout_ms):
            break
    robot.attach_right_motor.hold()