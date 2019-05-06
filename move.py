import pygame, sys, time, random
from pygame.locals import *

class Move:
  def __init__(self, name, moveType, power, accuracy, hpGain):
    self.__name = str(name)
    self.__moveType = moveType
    self.__power = power
    self.__accuracy = accuracy
    self.__hpGain = hpGain

  def __str__(self):
    return "Your move is called " + self.__name + ", its type is " + str(self.__moveType) + ", \n its power is " + str(self.__power) + ", its accuracy is " + str(self.__accuracy) + ", \n and it regains " + str(self.__hpGain) + "% of your HP \n"

  def getName(self):
    return self.__name

  def getPower(self):
    return self.__power

  def getType(self):
    return self.__moveType

  def getRegain(self):
    return self.__hpGain

  def hit(self):
    hitNum = random.randint(1,100)
    hitRange = 100 - self.__accuracy
    if hitNum >= hitRange:
      doesHit = True
    else:
      doesHit = False
    return doesHit
