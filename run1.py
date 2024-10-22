from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import move_functions



def run1 (ev3, walter, attach_left_motor, attach_right_motor):
#unexpected encounter
    walter.straight(300)
    walter.turn(-55)
    walter.straight(175)
    walter.straight(-165)
    walter.turn(50)
#krill_numero_uno
    walter.straight(75)
    walter.turn(40)
#change_shipping_lanes
    attach_left_motor.run_time(-700, 700, Stop.COAST, wait=True)
    walter.straight(50)
    attach_left_motor.run_angle(300, 30, Stop.HOLD, wait=True)
    walter.turn(45)
    attach_left_motor.run_angle(75, -10, Stop.COAST, wait=True)
    ev3.speaker.beep(500,200)
    walter.straight(-50)
    attach_left_motor.run_angle(300, 180, Stop.COAST, wait=True)
#get_the_krill+sample
    walter.turn(-60)
    wait(3000)
    walter.straight(390)
    walter.straight(-170)
    walter.turn(-70)
    walter.straight(70)
    walter.straight(-10)
    walter.turn(165)
    walter.straight(100)
    walter.straight(-200)
    walter.turn(85)
    walter.straight(350)