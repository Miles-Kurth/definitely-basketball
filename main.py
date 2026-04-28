#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor, TouchSensor
from pybricks.parameters import Port,Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.iodevices import I2CDevice
from pybricks.parameters import Color
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



def cutDecimal(numStr, keepPlaces):
    if float(numStr) < 10:
        return " " + numStr[0:2 + keepPlaces]
    else:
        return numStr[0:3 + keepPlaces]


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


pixels = []

ev3.screen.clear()

loadingProgress = 0
LPIncreasePerIncrement = 100.0/177 + 0.0001

for x in range(SCREENWIDTH):
    row = []
    for y in range(SCREENHEIGHT):
        pixel = Pixel(x, y, Color.WHITE)
        row.append(pixel)
        
        ev3.screen.draw_pixel(x,y)
    
    row.append(y)
    loadingProgress += LPIncreasePerIncrement
    toPrint = str(loadingProgress)
    ev3.screen.print("loading...   " + cutDecimal(toPrint,2) + "%")
# end loop

ev3.screen.clear()
ev3.screen.print("\n\n           100%")
drawScreenBorder()
wait(500)

clearScreen()

while True:
    pass


#clear random pixels, try to avoid repeats
#goal is efficiency





