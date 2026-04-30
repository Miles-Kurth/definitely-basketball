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
from random import betavariate


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
    
    def setColor(colorNew):
        self.color = colorNew


# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize motors
motor1 = Motor(Port.A)
motor2 = Motor(Port.B)

# Initialize sensors
fanButton = TouchSensor(Port.S4)
pongButton = TouchSensor(Port.S1)



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
    ev3.screen.clear()
    ev3.screen.print("\n\n            FAN")
    wait(500)
    clearScreen()
    ev3.screen.print("\n       don't worry\n          about it")
    speed = 7
    while True:
        if (speed > 100):
            speed = 100
        # print(speed)

        run()

        if (fanButton.pressed()):
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


def makePixel(x,y):
    pixel = Pixel(x, y, Color.WHITE)
    return pixel

def getRandomPixel():
    x = random.randint(0,SCREENWIDTH-1)
    y = random.randint(0,SCREENHEIGHT-1)
    pixel = pixels[y][x]
    return pixel

def drawPixel(x,y): # to black
    pixel = Pixel(x, y, Color.BLACK)
    pixels[y][x] = pixel
    ev3.screen.draw_pixel(x,y,Color.BLACK)

def erasePixel(x,y): # to white
    pixel = Pixel(x, y, Color.WHITE)
    pixels[y][x] = pixel
    ev3.screen.draw_pixel(x,y,Color.WHITE)

def togglePixel(x,y):
    print(pixels[y][x].getColor())
    if (pixels[y][x].getColor() == Color.WHITE):
        drawPixel(x,y)
    else:
        erasePixel(x,y)



# At start
ev3.speaker.set_volume(40); #ev3.speaker.beep(660,200)
ev3.speaker.beep(440)
halfStep = 2.0 ** (1.0/12)


# CODE BELOW

ev3.screen.print("\nred button for fan")
ev3.screen.print("\nblack button\nfor pong")
while True:
    if fanButton.pressed():
        fan()
        sys.exit()
    if pongButton.pressed():
        break
    wait(1)



ev3.screen.clear()

ev3.screen.print("\n\n        loading...")

pixels = [[makePixel(x,y) for x in range(SCREENWIDTH+1)] for y in range(SCREENHEIGHT+1)]



loadingProgress = 0
LPIncreasePerIncrement = 100.0/127 + 0.0001

# for y in range(SCREENHEIGHT):
#     # row = []

#     for x in range(SCREENWIDTH):
        
#         row.append(pixel)
        
#         ev3.screen.draw_pixel(x,y)
    
#         pixels[y][x] = 

#     loadingProgress += LPIncreasePerIncrement
#     toPrint = str(loadingProgress)
#     ev3.screen.print("loading...   " + cutDecimal(toPrint,2) + "%")

# end loop

ev3.screen.clear()
ev3.screen.print("\n\n           100%")
drawScreenBorder()

wait(500)

for i in range(1): #check array is filled, runs ONCE
    y = len(pixels)
    x = len(pixels[y-1])
    print("height=" + str(y) + " " + "width=" + str(x) )
    print("max Y=" + str(y-1) + " " + "max X=" + str(x-1) )

# for i in range(5000):
#     y = random.randint(38,89)
#     x = random.randint(38,139)
#     togglePixel(x,y)

# wait(500)

clearScreen()

wait(1000)

ev3.screen.print("\n\n           Sike")

for i in range(5000):
    y = random.betavariate(2,2)
    print(y)
    # y = random.randint(0,SCREENHEIGHT)
    # x = random.randint(0,SCREENWIDTH)
    # togglePixel(x,y)

fan()



#clear random pixels, try to avoid repeats
#goal is efficiency





