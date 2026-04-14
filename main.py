#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor, TouchSensor
from pybricks.parameters import Port,Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.iodevices import I2CDevice
import time
import sys


class LaserSensor:
    def __init__(self, port):
        self.i2c = I2CDevice(port, 0x02 >> 1)
        self.last_time = 0
        self.last_dist = 0

    def distance(self):
        now = time.time()
        if now - self.last_time > 0.03:
            self.last_time = now
            results = self.i2c.read(0x42, 2)
            self.last_dist = results[0] + (results[1] << 8)
        return self.last_dist


# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize motors
motor1 = Motor(Port.A)
motor2 = Motor(Port.B)

# Initialize sensors
button = TouchSensor(Port.S1)


# At start
ev3.speaker.set_volume(40); #ev3.speaker.beep(660,200)
ev3.speaker.beep(440)

def run():
    motor1.dc(100)
    motor2.dc(-100)

def brake():
    motor1.brake()
    motor2.brake()


# CODE BELOW

isRunning = False


while True:
    if (button.pressed()):
        if (isRunning == False):
            run()
        isRunning = True
    else:
        if (isRunning == True):
            brake()
        isRunning = False




