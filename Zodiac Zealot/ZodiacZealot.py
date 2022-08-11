
from pickle import TRUE
import random

class Character:
    def __innit__(self, name, health, mythicEnergy, defense, dodge, gold):
        self.name = name
        self.health = health
        self.mythicEnergy = mythicEnergy
        self.defense = defense
        self.dodge = dodge
        self.gold = gold

    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

    def attack(self, enemy):
        if enemy.evade():
            print(f'{enemy.name} has dodged!')
        else:
            hit = self.mythicEnergy - enemy.defense
            if hit <= 0:
                hit = 1
            enemy.health -= hit
            print(f' You hit {enemy.name} for {hit} damage!')
            if not enemy.alive():
                print(f'{enemy.name} dies!')
    def printStats(self):
        print('{} has {} Health{} Mythic Energy {}Defense'.format(self.name,self.health,self.defense))

    def evade(self):
        chanceRoll = random.randint(0,20)
        if self.dodge > chanceRoll:
            return True
        else:
            return False

class Zealot(Character):
    def __innit__(self, name, health, mythicEnergy, defense, dodge, gold, playerItems=[]):
        self.playerItems = playerItems
        super(Zealot,self). __innit__(name, health, mythicEnergy, defense, gold, dodge)
    def attack(self, enemy):
        if enemy.dodge():
            print(f'{enemy.name} dodged the attack!')
        else:
            chanceRoll = random.randint(0, 5)
            if chanceRoll == 0:
                hit = self.mythicEnergy * 2 - enemy.defense
                print('Mega power')
                print(f'You do {hit} damage to {enemy.name}')
        
            else:
                hit = self.mythicEnergy - enemy.defense
                if hit <= 0:
                    hit = 1
                enemy.health -= hit
                print(f'You hit {enemy.name} for {hit} damage!')
            if not enemy.alive():
                print(f'{enemy.name} dies!')
                print(f'You gain {enemy.gold} gold.')
                self.gold += enemy.gold
                print(f"You absorb some of the {enemy.name}'s Mythical Power, what attribute do you want to add to?")
                lvlup = input('''
                1.Attack
                2.Defense''' )
                while lvlup!= '1' and lvlup != '2':
                    input('Please choose Attack (1) or Defense(2).')
                if lvlup == '1':
                    self.mythicEnergy += 5  
                elif lvlup == '2':
                    self.defense += 5

#
class Enemy_1(Character):
class Enemy_2(Enemy_1):
class Enemy_3(Enemy_1):
class enemy_4(Enemy_1):


capricorn = Enemy_1('Capricorn: The Goat', 25, 5, 5, 0, 25 )
sagittarius = ('Sagittarius: The Centaur',)
scorpio = ('Scorpio: The Scorpion',)
libra = ('Libra: The Scales',)
virgo = ('Virgo The Virgin',)
leo = ('Leo: The Lion',)
gemini = Enemy4('Gemini: The twins',)
cancer = ('Cancer The Crab',)
taurus = Enemy4('Taurus:The Bull',)
aries = ('Aries: The Ram',)
pisces = ('Pisces: The Fish',)
aquarius = ('Aquarius: The Water Bearer',)

zodiac = {
    '1': capricorn,
    '2': sagittarius,
    '3': scorpio,
    '4' : libra,
    '5': virgo,
    '6': gemini,
    '7': cancer,
    '8': taurus,
    '9': aries,
    '10': pisces,
    '11': aquarius,
    '12': leo,
}


RESTRICTION_ON = True