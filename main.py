import random
import math
from computer import Computer
from pokemon import Pokemon
from move import Move

pkmnNames = ["Venusaur","Sceptile","Tropius","Chandelure","Camerupt","Arcanine","Gyarados","Blastoise","Milotic","Nidoking","Flygon","Mamoswine","Jolteon","Galvantula","Vikavolt","Pidgeot","Altaria","Aerodactyl","Lapras","Articuno","Walrein", "Agron", "Tyranitar", "Onix", "Salazzle", "Tentacool", "Naganadel", "Gengar", "Banette", "Giratina"]

class Play:
  def __init__(self, party1, party2):
    self.__pokemon1 = party1[0]
    self.__pokemon2 = party2[0]
    self.__party1 = party1
    self.__party2 = party2

  def initAtt(self):
    #chooses who is first and who is second in attack order
    if self.__pokemon1.getSpeed() >= self.__pokemon2.getSpeed():
      self.__att1 = self.__pokemon1
      self.__att2 = self.__pokemon2
      self.__p1F = True
    else:
      self.__att1 = self.__pokemon2
      self.__att2 = self.__pokemon1
      self.__p1F = False
    return self.__p1F

  def switch(self):
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
    self.__pokemon2 = party2[0]

  def useMove(self):
    #uses a... move?
    player1move = self.__att1.chooseMove()
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
      print("Your attack missed!")
    elif doesHit == True:
      dmg = ((22 * player1move.getPower() * (self.__att1.getAttack() / self.__att2.getDefense()))/50)
      if player1move.getPower() != 0:
        dmg += 2
      dmg *= damageMult
      dmg = round(dmg)
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

  def doWhat(self):
    x = input(self.__att1.getName() + ", what do you want to do? Enter [Attack] or [Switch].")
    if x == "Attack":
      self.useMove()
    elif x == "Switch":
      self.switch()

  def switchTurn(self):
    #swtiches the turn :)
    if self.__p1F == True:
      self.__att1 = self.__pokemon2
      self.__att2 = self.__pokemon1
      self.__p1F = False
    elif self.__p1F == False:
      self.__att1 = self.__pokemon1
      self.__att2 = self.__pokemon2
      self.__p1F = True


#Moves


#Chipper Team - gyarados, lapras, absol, tyranitar, chandelure, sceptile
#Jeremy's Team - gardevoir, aggron, absol, flygon, camerupt, sceptile

#Pokemon and stats
#Water
samurott = Pokemon("Samurott", "Water", "No")


pkmnObjects = [venusaur,sceptile,tropius,chandelure,camerupt,arcanine,gyarados,blastoise,milotic,nidoking,flygon,mamoswine,jolteon,galvantula,vikavolt,pidgeot,altaria,aerodactyl,lapras,articuno,walrein,tyranitar,aggron,tentacruel,naganadel,salazzle,gengar,banette,giratina,volcorona,steelix,ribombee,medicham,garchomp,dragonite,metagross,gardevoir,mew,absol,empoleon]

allPkmnNames = ''
hold = 0
pType = 1
for x in pkmnObjects:
  if x.getType2() == 'No':
    allPkmnNames = allPkmnNames  + x.getName() + ": " + x.getType() + ". "
  else:
    allPkmnNames = allPkmnNames  + x.getName() + ": " + x.getType() + ", " + x.getType2() + ". "
  hold += 1
  if hold == 5:
    allPkmnNames.strip(" ----- ")
    allPkmnNames += "\n"
    hold = 0

party1 = []
party2 = []
print("Player 1: What 6 Pokemon do you want to use? Your choices are: \n" + allPkmnNames)
for x in range(6):
  pokemon1 = input("")
  for y in pkmnObjects:
    if y.getName() == pokemon1:
      pokemon1 = y
      party1.append(pokemon1)
      break
print("Player 2: What 6 Pokemon do you want to use? Your choices are: \n" + allPkmnNames)
for x in range(6):
  pokemon2 = input("")
  for y in pkmnObjects:
    if y.getName() == pokemon2:
      pokemon2 = y
      party2.append(pokemon2)
      break
game = Play(party1,party2)
game.initAtt()
while party1 != [] and party2 != []:
  game.doWhat()
  game.switchTurn()
