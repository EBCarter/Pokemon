import pygame, sys, time, random
from pygame.locals import *

class Pokemon:

  def __init__(self, name, x, y, pkmnType, type2, maxhp, attack, defense, speed, move1, move2, move3, move4, image):
    self.x = x
    self.y = y
    self.__pkmnType = pkmnType
    self.__type2 = type2
    self.__name = name
    self.__maxhp = maxhp
    self.__hp = maxhp
    self.__attack = attack
    self.__defense = defense
    self.__speed = speed
    self.__move1 = move1
    self.__move2 = move2
    self.__move3 = move3
    self.__move4 = move4
    self.image = image
    self.rect = pygame.Rect(self.x, self.y, 50, 50)

  def __str__(self):

    return str(self.__name) + ". It's type is " + str(self.__pkmnType) + ", it has " + str(self.__hp) + " hit points,\nhas an attack stat of " + str(self.__attack) + ",has a defense stat of " + str(self.__defense) + ",and has a speed stat of " + str(self.__speed) + "\n"

  def getName(self):
    return self.__name

  def getHP(self):
    return self.__hp

  def getMove1(self):
      return self.__move1

  def getMove2(self):
      return self.__move2

  def getMove3(self):
    return self.__move3

  def getMove4(self):
      return self.__move4

  def getType(self):
    return self.__pkmnType

  def getType2(self):
    return self.__type2

  def getAttack(self):
    return self.__attack

  def getDefense(self):
    return self.__defense

  def getSpeed(self):
    return self.__speed

  def gainHP(self, move):
    gain = move.getRegain()
    gain *= (self.getHP() / 100)
    round(gain)
    self.__hp += gain
    if self.__hp > self.__maxhp:
      self.__hp = self.__maxhp
    round(self.__hp)

  def userChooseMove(self):
    move_choice = self.getName() + ", which move do you want to use? Enter the number \n 1): " + self.__move1.getName() + "\n 2): " + self.__move2.getName() + "\n 3): " + self.__move3.getName() + "\n 4): " + self.__move4.getName() + "\n"

    if move_choice == "1":
      return self.__move1
    elif move_choice == "2":
      return self.__move2
    elif move_choice == "3":
      return self.__move3
    elif move_choice == "4":
        return self.__move4

  def choosePokemon(pkmnList):
    choice = random.randint(0, (len(pkmnList)-1))
    return choice

  def chooseMove(self, compPkmn):
      choice = random.randint(1,4)
      if choice == 1:
        return compPkmn.__move1
      elif choice == 2:
        return compPkmn.__move2
      elif choice == 3:
        return compPkmn.__move3
      elif choice == 4:
          return compPkmn.__move4

  def loseHealth(self, dmg, move, user, comp, turn):
    print = ""
    if dmg == 0 and move.getRegain() > 0:
      print = str(pokemon2.getName()) + " regained " + str(move.getRegain()) + "% of its HP! Its current HP is " + str(pokemon2.getHP()) + "."
    elif dmg == 0:
      print = "It had no effect..."
    elif dmg > 0 and move.getRegain() > 0:
      print = str(self.getName()) + " took " + str(dmg) + " damage! Its current HP is " + str(self.getHP()) + "." + str(pokemon2.getName()) + " regained " + str(move.getRegain()) + "% of its HP! Its current HP is " + str(pokemon2.getHP()) + "."
    else:
      if turn == False:
        user.__hp -= dmg
        print = str(user.getName()) + " took " + str(dmg) + " damage! Its current HP is " + str(self.getHP()) + "."
      elif turn == True:
        comp.__hp -= dmg
        print = str(comp.getName()) + " took " + str(dmg) + " damage! Its current HP is " + str(comp.getHP()) + "."
    return print
