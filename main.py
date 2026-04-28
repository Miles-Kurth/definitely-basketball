#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor, TouchSensor
from pybricks.parameters import Port,Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.iodevices import I2CDevice
import time
import sys
import math


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



SCREENWIDTH = 177
SCREENHEIGHT = 127
PLAYBOUNDSX = SCREENWIDTH - 1
PLAYBOUNDSY = SCREENHEIGHT - 1

speed = 7

def run():
    motor1.dc(-speed)
    motor2.dc(speed)

def brake():
    motor1.brake()
    motor2.brake()

def fan():
    while True:
        if (speed > 100):
            speed = 100
        print(speed)

        run()

        if (button.pressed()):
            speed += 0.03 + (speed *0.001)
        else:
            speed += -0.2
            if (speed <= 7):
                speed = 7
                brake()    



def clearScreen():
    ev3.screen.clear()


def touchingLeft(x,y):
    if (x == 1):
        return True
    return False

def touchingRight(x,y):
    if (x == PLAYBOUNDSX):
        return True
    return False

def touchingTop(x,y):
    if (y == 1):
        return True
    return False

def touchingBottom(x,y):
    if (y == PLAYBOUNDSY):
        return True
    return False

def touchingH(x,y):
    if (touchingLeft(x,y) or touchingRight(x,y)):
        return True
    return False

def touchingV(x,y):
    if (touchingTop(x,y) or touchingBottom(x,y)):
        return True
    return False

def touchingEdge(x,y):
    if (touchingH(x,y) or touchingV(x,y)):
        return True
    return False

def drawRandomPixel():
    x = random.randint(0,SCREENWIDTH)
    y = random.randint(0,SCREENHEIGHT)
    ev3.screen.draw_pixel(x,y,Color.BLACK)
    ev3.screen.draw_box(1,1,SCREENWIDTH,SCREENHEIGHT,0,False)

def eraseRandomPixel():
    x = random.randint(0,SCREENWIDTH)
    y = random.randint(0,SCREENHEIGHT)
    ev3.screen.draw_pixel(x,y,Color.WHITE)
    ev3.screen.draw_box(1,1,SCREENWIDTH,SCREENHEIGHT,0,False)

# At start
ev3.speaker.set_volume(40); #ev3.speaker.beep(660,200)
ev3.speaker.beep(440)


# CODE BELOW

pixels = []


clearScreen()
for y in range(SCREENHEIGHT):
    row = []
    for x in range(SCREENWIDTH):
        ev3.screen.draw_pixel(x,y,Color.BLACK)
        row.append(x)
    row.append(y)
#end loop

clearScreen()

ev3.screen.draw_box(1,1,SCREENWIDTH,SCREENHEIGHT,0,False)

while True:
    pass


    





