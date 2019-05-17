import random
import math
import pygame, sys, time, random
from pygame.locals import *
from pokemon import Pokemon
from move import Move

#Always call before utilizing pygame functions
pygame.init()

#make the background
#background_image = pygame.image.load('')

#the images
samurott_image = pygame.image.load('samurott.png')
torterra_image = pygame.image.load('torterra.png')
typhlosion_image = pygame.image.load('typhlosion.png')
title_screen = pygame.image.load('pokemon-background.png')
battle_screen = pygame.image.load('battle-scene.png')

#Sets FPS and starts game clock/
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((900,500), 0, 32)
#Sets title of GUI frame
pygame.display.set_caption("Pokemon Battle Simultaor")

#Sets background color
WHITE = (250, 250, 250)
BLUE = (0,0,250)

pkmnNames = ["Torterra", "Samurott", "Typhlosion"]

class Play:
  def __init__(self, userPkmn, compPkmn):
    '''self.__pokemon1 = party1[0]
    self.__pokemon2 = party2[0]
    self.__party1 = party1
    self.__party2 = party'''
    self.user = userPkmn
    self.comp = compPkmn

  def initAtt(self):
    #chooses who is first and who is second in attack order
    if self.user.getSpeed() >= self.comp.getSpeed():
      self.__att1 = self.user
      self.__att2 = self.comp
      self.__p1F = True
      print("You go first.")
    else:
      self.__att1 = self.comp
      self.__att2 = self.user
      self.__p1F = False
      print("The computer goes first.")
    return self.__p1F

  """def switch(self):
    x = self.initAtt()
    if x == True:
      party = self.__party1
    elif x == False:
      party = self.__party2
    print("Who do you want to switch in to? Your party is: ")
    for x in party:
      print(x.getName())
    switch = input("")
    for x in party:
      if x.getName() == switch:
        y = x
        party.remove(x)
        party.insert(y,0)
    self.__pokemon1 = party1[0]
    self.__pokemon2 = party2[0]"""

  def useMove(self):
    #uses a... move?
    print("-------------------------------------------")
    if self.__p1F == True:
        player1move = self.__att1.userChooseMove()
    elif self.__p1F == False:
        player1move = self.__att1.chooseMove()
    #player1move = self.__att1.userChooseMove()


    doesHit = player1move.hit()
    damageMult = 1
    dmg = 0
    type1or2 = [self.__att2.getType(), self.__att2.getType2()]
    for x in type1or2:
      if x == self.__att2.getType2() and x == "No":
        damageMult *= 1
      if player1move.getType() == "Normal" and (self.__att2.getType() == "Ghost" or self.__att2.getType2() == "Ghost"):
        damageMult = 0
      else:
        if player1move.getType() == "Water":
          if x == "Fire" or x == "Ground" or x == "Rock":
            damageMult *= 2
          elif x == "Grass" or x == "Water" or x == "Ice":
            damageMult *= 0.5
        elif player1move.getType() == "Fire":
          if x == "Grass" or x == "Ice" or x == "Bug" or x == "Steel":
            damageMult *= 2
          elif x == "Water" or x == "Fire" or x == "Rock" or x == "Dragon":
            damageMult *= 0.5
        elif player1move.getType() == "Grass":
          if x == "Water" or x == "Ground" or x == "Rock":
            damageMult *= 2
          elif x == "Flying" or x == "Fire" or x == "Grass" or x == "Poison" or x == "Bug" or x == "Steel" or x == "Ice":
            damageMult *= 0.5
        elif player1move.getType() == "Ground":
          if x == "Electric" or x == "Fire" or x == "Rock" or x == "Poison" or x == "Steel":
            damageMult *= 2
          elif x == "Grass" or x == "Bug":
            damageMult *= 0.5
          elif x == "Flying":
            damageMult *= 0
        elif player1move.getType() == "Electric":
          if x == "Water" or x == "Flying":
            damageMult *= 2
          elif x == "Electric" or x == "Grass" or x == "Dragon":
            damageMult *= 0.5
          elif x == "Ground":
            damageMult *= 0
        elif player1move.getType() == "Flying":
          if x == "Grass" or x == "Bug" or x == "Fighting":
            damageMult *= 2
          elif x == "Electric" or x == "Rock" or x == "Steel":
            damageMult *= 0.5
        elif player1move.getType() == "Ice":
          if x == "Grass" or x == "Flying" or x == "Ground" or x == "Dragon":
            damageMult *= 2
          elif x == "Fire" or x == "Water" or x == "Ice" or x == "Steel":
            damageMult *= 0.5
        elif player1move.getType() == "Rock":
          if x == "Fire" or x == "Flying" or x == "Ice" or x == "Bug":
            damageMult *= 2
          elif x == "Ground" or x == "Fighting" or x == "Steel":
            damageMult *= 0.5
        elif player1move.getType() == "Poison":
          if x == "Grass" or x == "Fairy":
            damageMult *= 2
          elif x == "Poison" or x == "Ground" or x == "Rock" or x == "Ghost":
            damageMult *= 0.5
        elif player1move.getType() == "Ghost":
          if x == "Ghost" or x == "Psychic":
            damageMult *= 2
          elif x == "Poison":
            damageMult *= 2
        elif player1move.getType() == "Psychic":
          if x == "Fighting" or x == "Poison":
            damageMult *= 2
          elif x == "Steel" or x == "Psychic":
            damageMult *= .5
          elif x == "Dark":
            damageMult *= 0
        elif player1move.getType() == "Bug":
          if x == "Grass" or x == "Psychic" or x == "Dark":
            damageMult *= 2
          elif x == "Fighting" or x == "Flying" or x == "Poison" or x == "Ghost" or x == "Steel" or x == "Fire" or x == "Fairy":
            damageMult *= .5
        elif player1move.getType() == "Fairy":
          if x == "Dragon" or x == "Fighting" or x == "Dark":
            damageMult *= 2
          elif x == "Poison" or x == "Steel" or x == "Fire":
            damageMult *= .5
        elif player1move.getType() == "Fighting":
          if x == "Rock" or x == "Steel" or x == "Ice" or x == "Dark":
            damageMult *= 2
          elif x == "Flying" or x == "Poison" or x == "Bug" or x == "Fairy" or x == "Psychic":
            damageMult *= .5
          elif x == "Ghost":
            damageMult *= 0
        elif player1move.getType() == "Dark":
          if x == "Psychic" or x == "Ghost":
            damageMult *= 2
          elif x == "Fighting" or x == "Dark" or x == "Fairy":
            damageMult *= .5
        elif player1move.getType() == "Dragon":
          if x == "Dragon":
            damageMult *= 2
          elif x == "Steel":
            damageMult *= .5
          elif x == "Fairy":
            damageMult *= 0
        elif player1move.getType() == "Steel":
          if x == "Rock" or x == "Ice" or x == "Fairy":
            damageMult *= 2
          elif x == "Steel" or x == "Fire" or x == "Water" or x == "Electric":
            damageMult *= .5

    if doesHit == False:
      dmg = 0
      if self.__p1F == True:
          print("Your attack missed!")
      elif self.__p1F == False:
          print(str(compPkmn.getName()) + "\'s attack missed")
    elif doesHit == True:
      dmg = ((22 * player1move.getPower() * (self.__att1.getAttack() / self.__att2.getDefense()))/50)
      if player1move.getPower() != 0:
        dmg += 2
      dmg *= damageMult
      dmg = round(dmg)
      if self.__p1F == True:
          print("Your pokemon used " + str(player1move.getName()))
      elif self.__p1F == False:
          print(str(compPkmn.getName()) + " used " + str(player1move.getName()))
      self.__att1.gainHP(player1move)
      self.__att2.loseHealth(dmg,player1move, self.__att1)
      if self.__att2.getHP() <= 0:
        print(self.__att2.getName() + " fainted!")
        self.__party2.remove(self.__att2)
      if damageMult > 1:
        print("It's super effective!")
      elif damageMult < 1:
        print("It's not very effective...")
    if player1move.getPower() == 0:
      dmg = 0

  '''def doWhat(self):
    x = input(self.__att1.getName() + ", what do you want to do?")
    #x = x.capitalize()
    if x.capitalize() == "Attack":
      self.useMove()
    elif x == "Switch":
      self.switch()'''

  def switchTurn(self):
    #swtiches the turn :)
    if self.__p1F == True:
      self.__att1 = self.comp
      self.__att2 = self.user
      self.__p1F = False
    elif self.__p1F == False:
      self.__att1 = self.user
      self.__att2 = self.comp
      self.__p1F = True

#Moves
#Water
samurrise = Move("Samur-Rise", "Water", 50, 95, 0)
condense = Move("Condense", "Water", 20, 90, 30)
hydro = Move("Hydro", "Water", 40, 100, 0)
#Normal
fortnite = Move("Fortnite", "Normal", 90, 50, 0)
#Grass
bramble = Move("Bramble", "Grass", 40, 100, 0)
turtle = Move("Turtle", "Grass", 0, 100, 40)
#Ground
spiked = Move("Spiked", "Ground", 60, 65, 0)
#Fire
fire_tornado = Move("Fire Tornado", "Fire", 50, 90, 0)
engulf = Move("Engulf", "Fire", 0, 95, 40)
chicago = Move("Chicago", "Fire", 45, 100, 0)

#Pokemon and stats
#Water
samurott = Pokemon("Samurott", 10, 100, "Water", "No", 120, 40, 50, 50, samurrise, condense, hydro, fortnite, samurott_image)

#Grass
torterra = Pokemon("Torterra", 50, 100, "Grass", "Ground", 150, 45, 60, 30, bramble, turtle, spiked, fortnite, torterra_image)

#Fire
typhlosion = Pokemon("Typhlosion", 90, 100, "Fire", "No", 110, 55, 40, 45, fire_tornado, engulf, chicago, fortnite, typhlosion_image)


pkmnObjects = [torterra, samurott, typhlosion]
allPkmnNames = ''
hold = 0
pType = 1
userPkmn = torterra

'''userChoice = input("What Pokemon do you want to use? Your choices are: \n" + str(pkmnNames) + "\n")
userChoice = userChoice.capitalize()
compChoice = Pokemon.choosePokemon(pkmnObjects)
compPkmn = pkmnObjects[compChoice]
for y in pkmnObjects:
    if y.getName() == userChoice:
        #print("MATCH")
        userPkmn = y
        break
for x in range(len(pkmnObjects)):
    print(x)
    print(compChoice)
    if compPkmn == userPkmn:
        compChoice = Pokemon.choosePokemon(pkmnObjects)
        compPkmn = pkmnObjects[compChoice - 1]


game = Play(userPkmn, compPkmn)
print("Your Pokemon is " + str(userPkmn) + "The computers Pokemon is " + str(compPkmn))
game.initAtt()'''
#while userPkmn.getHP() > 0:
  #game.useMove()
  #game.switchTurn()

BASICFONT = pygame.font.Font('freesansbold.ttf',16)
text = "What Pokemon do you want to use? To choose Samurott, press left." \
        " To choose Typhlosion press up. To choose Torterra press right."
print = BASICFONT.render(text,1,(0,0,0))
Rect = print.get_rect()
Rect.topleft = (50, 400)
chosenPkmn = False

#start game loop
while True:
    DISPLAYSURF.fill((0,0,0))
    background = pygame.transform.scale(title_screen,(900, 500))
    battlescene = pygame.transform.scale(battle_screen,(900, 500))
    #DISPLAYSURF.blit(background,(0, 0))

    if chosenPkmn == False:
        DISPLAYSURF.blit(background,(0,0))

    if chosenPkmn == True and userPkmn.getHP() > 0:
        DISPLAYSURF.blit(battlescene,(0,0))

    DISPLAYSURF.blit(print, Rect)

    for event in pygame.event.get():
        #the quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:

            if event.key == K_RIGHT:
                userChoice = torterra

            elif event.key == K_LEFT:
                userChoice = samurott

            elif event.key == K_UP:
                userChoice = typhlosion

    #update display
    pygame.display.update()
    fpsClock.tick(FPS)
