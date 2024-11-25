from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Container:

    def __init__(self):
        self.ev3 = EV3Brick()
        self.left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.attach_left_motor = Motor(Port.A)
        self.attach_right_motor = Motor(Port.D)
        self.walter = DriveBase(self.left_motor, self.right_motor, 62.4, 98.4)
        self.gyro = GyroSensor(Port.S1)
        self.color_sensor_right = ColorSensor(Port.S2)
        self.color_sensor_left = ColorSensor(Port.S3)