import sys
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

class Container:

    def display_error(self, message):
        self.ev3.screen.clear()
        self.ev3.screen.set_font(Font(family=None, size=20, bold=False, monospace=False, lang=None, script=None))
        self.ev3.screen.draw_text(0,60, message)
        self.ev3.light.on(Color.RED)
        wait(4000)
        sys.exit()

    def __init__(self):
        self.ev3 = EV3Brick()

        try:
            self.left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        except:
            self.display_error("Check left motor(B)")
            

        try:
            self.right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        except:
            self.display_error("Check right motor(C)")

        try:
            self.attach_left_motor = Motor(Port.A)
        except:
            self.display_error("Check Claw (A)")
        
        try:
            self.attach_right_motor = Motor(Port.D)
        except:
            self.display_error("Check Stick (D)")

        try:
            self.gyro = GyroSensor(Port.S1)
        except:
            self.display_error("Check Gyro (1)")

        try:
            self.color_sensor_right = ColorSensor(Port.S2)
        except:
            self.display_error("Check Right Color (2)")

        try:
            self.color_sensor_left = ColorSensor(Port.S3)
        except:
            self.display_error("Check Left Color (3)")

        self.walter = DriveBase(self.left_motor, self.right_motor, 62.4, 98.4)

        #check gyro value before first run
        gyro1 = self.gyro.angle()
        wait(500)
        gyro2 = self.gyro.angle()
        if gyro1 - gyro2 > 3:
           self.display_error("calibrate gyro")
        if gyro1 - gyro2 < -3:
           self.display_error("calibrate gyro")

        

    