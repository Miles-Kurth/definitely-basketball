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


class Pixel:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getColor(self):
        return self.color
    
    def setColor(color):
        self.color = color


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



def run():
    motor1.dc(-speed)
    motor2.dc(speed)

def brake():
    motor1.brake()
    motor2.brake()

def fan():
    speed = 7
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
    drawScreenBorder()

def drawScreenBorder():
    ev3.screen.draw_box(1,1,SCREENWIDTH,SCREENHEIGHT,0,False)


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


def drawPixel(): # to black
    x = random.randint(0,SCREENWIDTH)
    y = random.randint(0,SCREENHEIGHT)
    pixels[y][x].setColor(Color.BLACK)
    drawScreenBorder()

def erasePixel(): # to white
    x = random.randint(0,SCREENWIDTH)
    y = random.randint(0,SCREENHEIGHT)
    pixels[y][x].setColor(Color.WHITE)
    drawScreenBorder()
def togglePixel(pixel):
    if (pixel.getColor() == Color.WHITE):
        pixel.setColor(Color.WHITE)
    else:
        puxel.setColor(Color.BLACK)


# At start
ev3.speaker.set_volume(40); #ev3.speaker.beep(660,200)
ev3.speaker.beep(440)
halfStep = 2.0 ** (1.0/12)


# CODE BELOW

pixels = []

ev3.screen.clear()
ev3.screen.print("loading...")

loadingPitch = 250


for y in range(SCREENHEIGHT):
    row = []
    for x in range(SCREENWIDTH):
        ev3.screen.draw_pixel(x,y,Color.BLACK)
        pixel = Pixel(x, y, Color.WHITE)
        row.append(pixel)
        loadingPitch += halfStep / (SCREENWIDTH/2)
    row.append(y)
    loadingPitch += halfStep * 5
#end loop

clearScreen()

ev3.screen.draw_box(1,1,SCREENWIDTH,SCREENHEIGHT,0,False)

while True:
    pass


#clear random pixels, try to avoid repeats
#goal is efficiency





