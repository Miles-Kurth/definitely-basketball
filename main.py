#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor, TouchSensor
from pybricks.parameters import Port,Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.iodevices import I2CDevice
from pybricks.parameters import Color
from decimal import *
import time
import sys
import math
import random


ran = random


class Pixel:
    def __init__(self, x, y, colorIn):
        self.x = x
        self.y = y
        self.color = colorIn

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getColor(self):
        return self.color
    
    def setColor(colorIn):
        self.color = colorIn


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





def fan():
    def run():
        motor1.dc(-speed)
        motor2.dc(speed)

    def brake():
        motor1.brake()
        motor2.brake()
    
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



def cutDecimal(num, keepPlaces):
    s = "0." 
    for i in range(keepPlaces):
        s += "0"
    s += "1"

    num2 = num - (num % float(s))
    return num2


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


def getRandomPixel():
    x = random.randint(0,SCREENWIDTH)
    y = random.randint(0,SCREENHEIGHT)
    pixel = pixels[y][x]
    return pixel

def drawPixel(pixel): # to black
    pixel.setColor(Color.BLACK)

def erasePixel(pixel): # to white
    pixel.setColor(Color.WHITE)

def togglePixel(pixel):
    if (pixel.getColor() == Color.WHITE):
        pixel.setColor(Color.BLACK)
    else:
        pixel.setColor(Color.WHITE)


# At start
ev3.speaker.set_volume(40); #ev3.speaker.beep(660,200)
ev3.speaker.beep(440)
halfStep = 2.0 ** (1.0/12)


# CODE BELOW

val = 123.4500
print(f"{val:g}")

pixels = []

ev3.screen.clear()

loadingProgress = Decimal('0')
LPIncreasePerRow = 0.78

for y in range(SCREENHEIGHT):
    row = []
    for x in range(SCREENWIDTH):
        pixel = Pixel(x, y, Color.WHITE)
        row.append(pixel)
        
        ev3.screen.draw_pixel(x,y)
        

    row.append(y)
    loadingProgress += LPIncreasePerRow
    ev3.screen.print("loading...   " + loadingProgress + "%")
#end loop



clearScreen()

ev3.screen.draw_box(1,1,SCREENWIDTH,SCREENHEIGHT,0,False)

while True:
    pass


#clear random pixels, try to avoid repeats
#goal is efficiency





