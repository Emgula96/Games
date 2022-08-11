
import random

#characters
class Character:
    def __init__(self, name, health, power, gold, armor, evade):
        self.name = name
        self.health = health
        self.power = power
        self.gold = gold
        self.armor = armor
        self.evade = evade

    def alive(self): 
        if self.health > 0:
            return True
        else:
            return False   

    def attack(self, other):
        if other.dodge():
            print(f"{other.name} has dodged! No damage.")
        else:
            hit = self.power - other.armor
            if hit <= 0:
                hit = 1
            other.health -= hit
            print(f"{self.name} does {hit} damage to {other.name}")
            if not other.alive():
                print(f"{other.name} has died!")

    def dodge(self):
        dice = random.randint(0, 20)
        if self.evade > dice:
            return True
        else:
            return False

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, name, health, power, gold, armor, evade, supplies=[]):
        self.supplies = supplies
        super(Hero, self).__init__(name, health, power, gold, armor, evade)
    
    def attack(self, other):
        if other.dodge():
            print(f"{other.name} has dodged! No damage.")
        else:
            dice = random.randint(0, 5)
            if dice == 0:
                hit = self.power * 2 - other.armor
                print("CRITICAL HIT!")
                print(f"{self.name} does {hit} damage to {other.name}")
                other.health -= hit
            else:
                hit = self.power - other.armor
                if hit <= 0:
                    hit = 1
                other.health -= hit
                print(f"{self.name} does {hit} damage to {other.name}")
            if not other.alive():
                print(f"{other.name} has died!")
                print(f"You gain {other.gold} gold.")
                self.gold += other.gold 

#
class Baddie(Character):
    def attack(self, other):
        if other.dodge():
            print(f"You dodge the attack! No damage.")
        else:
            hit = self.power - other.armor
            if hit <= 0:
                hit = 1
            other.health -= hit
            print(f"{self.name} does {hit} damage to you.")
            if not other.alive():
                print(f"{other.name} has died!")

class Zombie(Baddie):
    def __init__(self, name, health, power, gold, armor, evade, poisoned):
        super(Zombie, self).__init__(name, health, power, gold, armor, evade)
        self.poisoned = poisoned

    def alive(self):
        if self.poisoned == True:
            return False
        else:
            return True

class Medic(Baddie):
    def attack(self, other):
        heal = random.randint(1, 6)
        if heal == 5:
            self.health += 2
            print("The Medic has healed himself!")
            
        other.health -= self.power
        print(f"{self.name} does {self.power} damage to {other.name}")
        if not other.alive():
            print(f"{other.name} has died!")

class Ghoul(Baddie):
    def __init__(self, name, health, power, gold, armor, evade, canResurrect):
        self.canResurrect = canResurrect
        super(Ghoul, self).__init__(name, health, power, gold, armor, evade)
    
    def alive(self):
        if self.health > 0:
            return True
        
        if self.health < 0 and self.canResurrect:
            print(f"{self.name} is reviving!")
            self.canResurrect = False
            self.health = 15
            self.evade += 1
            self.armor += 1
            self.power += 2
            return True
        else:
            return False

class Slime(Baddie):
    def attack(self, other):
        if other.dodge():
            print(f"{other.name} has dodged! No damage.")
        else:
            chance = random.randint(0, 20)
            if chance <= 6:
                print(f"{self.name} slips and misses you! No damage.")
            elif chance <= 18:
                hit = self.power - other.armor
                if hit <= 0:
                    hit = 1
                other.health -= hit
                print(f"{self.name} does {hit} damage to {other.name}")
            else:
                hit = self.power * 2 - other.armor
                print("CRITICAL HIT!")
                print(f"{self.name} does {hit} damage to {other.name}!!!")

            if not other.alive():
                print(f"{other.name} has died!")


#items 
class Item():
    def __init__(self, restrictToFight):
        self.restrictToFight = restrictToFight
    
    def canUse(self, status):
        if self.restrictToFight:
            if status: 
                return False
            else:
                return True
        return True

class Tonic(Item):
    def use(self, recipient):
        recipient.health += 10
        print("Health goes up by 10!")

class MegaTonic(Tonic):
    def use(self, recipient):
        recipient.health += 20
        print("Health goes up by 20!")

class Poison(Item):
    def use(self, recipient):
        recipient.health -= 10
        print(f"{recipient.name} has been poisoned! Health at {recipient.health}")

class MegaPoison(Item):
    def use(self, recipient):
        recipient.health -= 20
        print(f"{recipient.name} has been MEGA poisoned! Health at {recipient.health}!")

class ZombiePoison(Item):
    def use(self, recipient):
        try:
            recipient.poisoned == True
            print(f"{recipient.name} has been ZOMBIE MEGA ULTRA GIGA POISONED! He gonna die now!")
        except:
            print("ZombiePoison only works on Zombies!")



# from characters import *

#hero
sigmund = Hero("Sigmund", 30, 5, 20, 0, 5, {})

#items
SuperTonic = Tonic(False)
SuperPoison = Poison(True)
mmegapoison = MegaPoison(True)
mmegatonic = MegaTonic(False)
zzombiepoison = ZombiePoison(True)

#baddies
goblin = Baddie("Blorg the Goblin", 20, 2, 5, 0, 0)
zombie = Zombie("Peter the Zombie", 10, 1, 100, 0, 0, False)
medic = Medic("Dr. Evil", 40, 1, 20, 3, 0)
shadow = Baddie("Frank the Shadow", 1, 1, 30, 0, 18)
ghoul = Ghoul("Steve the Ghoul", 50, 4, 30, 1, 2, True)
slime = Slime("Bill the Slime", 30, 2, 5, 0, 4)

baddies = {
    "1": goblin,
    "2": zombie,
    "3": medic,
    "4": shadow,
    "5": ghoul,
    "6": slime,
}




RESTRICTION_ON = True


import random 
# from characters import *
# from variables import *



def main(enemy):
    RESTRICTION_ON = False
    print("\n"*20)
    while enemy.alive() and sigmund.alive():
        
        sigmund.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. Attack")
        print("2. Use an Item")
        print("3. Flee\n")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            sigmund.attack(enemy)
        elif raw_input == "2":
            useItem(RESTRICTION_ON, enemy)
        elif raw_input == "3":
            print(f"Running away from {enemy.name}...")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health > 0:
            enemy.attack(sigmund)
        print("\n")
    
    RESTRICTION_ON = True 

    if not sigmund.alive():
        print("You have died! Goodbye.\n\n\n")
    else:
        camp()

def camp():
    print("\n")
    print("You are safe at the camp. What would you like to do?")
    print("""
    1. go to the shop
    2. go fighting
    3. check your stats
    4. use an item
    5. quit\n
    """)
    choice = input(">> ")
    if choice == "1":
        shop()
    elif choice == "2":
        baddie = input("""
    Who would you like to fight?
    1. goblin
    2. zombie
    3. medic
    4. shadow
    5. ghoul
    6. slime\n
    """)
        if int(baddie) <= len(baddies):
            main(baddies[baddie])
        else:
            camp()
    elif choice == "3":
        sigmund.print_status()
        print(f"You have {sigmund.gold} gold, {sigmund.armor} armor, {sigmund.evade} evade, and {sigmund.power} power.\n")
        print("----SUPPLIES----")
        for item in sigmund.supplies:
            print("\t" + item)
        if sigmund.supplies == {}:
            print("\n** There's nothing here! **")
        camp()
    elif choice == "4":
        useItem(RESTRICTION_ON)
        camp()
    elif choice == "5":
        print("Goodbye!")
    else:
        print("sorry, that wasn't a choice.")
        camp()

def shop():
    print(f"""\n\n\n
    Welcome to the shop.
    You currently have {sigmund.gold}gp.
    What would you like to purchase?
    
    1. Tonic - 10gp
    2. Poison - 10gp
    3. MegaPoison - 20gp
    4. MegaTonic - 20gp
    5. Armor Upgrade - 15gp
    6. Sword Upgrade - 15gp
    7. Evade Upgrade - 20gp
    8. ZombiePoison - 100gp
    9. Nothing

    \n""")
    myinput = input(">> ")
    if myinput == "1":
        if sigmund.gold >= 10:
            sigmund.gold -= 10
            sigmund.supplies["Tonic"] = SuperTonic
            print("One Tonic added to supplies!")
        else:
            print("Sorry, you do not have enough gold.")            
    elif myinput == "2":
        if sigmund.gold >= 10:
            sigmund.gold -= 10
            sigmund.supplies["Poison"] = SuperPoison
            print("One Poison added to supplies!")
    elif myinput == "3":
        if sigmund.gold >= 20:
            sigmund.gold -= 20
            sigmund.supplies["MegaPoison"] = mmegapoison
            print("One MegaPoison added to supplies!")
        else:
            print("Sorry, you do not have enough gold.") 
    elif myinput == "4":
        if sigmund.gold >= 20:
            sigmund.gold -= 20
            sigmund.supplies["MegaTonic"] = mmegatonic
            print("One MegaTonic added to supplies!")
        else:
            print("Sorry, you do not have enough gold.") 
    elif myinput == "5":
        if sigmund.gold >= 15:
            sigmund.gold -= 15
            sigmund.armor += 2
            print(f"You upgrade your armor. Your armor is now at level {sigmund.armor}.")
        else:
            print("Sorry, you do not have enough gold.") 
    elif myinput == "6":
        if sigmund.gold >= 15:
            sigmund.gold -= 15
            sigmund.power += 3
            print(f"You upgrade your skills. Your power is now at level {sigmund.power}.")
        else:
            print("Sorry, you do not have enough gold.")
    elif myinput == "7":
        if sigmund.gold >= 20:
            sigmund.gold -= 20
            sigmund.evade += 2
            print(f"You upgrade your skills. Your evade is now at level {sigmund.evade}.")
        else:
            print("Sorry, you do not have enough gold.") 
    elif myinput == "8":
        if sigmund.gold >= 100:
            sigmund.gold -= 100
            sigmund.supplies["ZombiePoison"] = zzombiepoison
            print("You just bought a ZombiePoison. It's about to get real.")
        else:
            print("Sorry, you do not have enough gold.") 
    else:
        pass
        
    print("Going back to the camp...\n")
    camp()

def useItem(s, enemy=None):
    if sigmund.supplies == {}:
        print("\nYou have no supplies!")
        return

    print("You have the following supplies: \n")
    for item in sigmund.supplies:
        print("\t" + item)
    itemchoice = input("What would you like to use? >> ")
    if itemchoice not in sigmund.supplies:
        print("I'm sorry, you don't have that.")
        return

    myitem = sigmund.supplies[itemchoice]
    if not myitem.canUse(s):
        print("You can't use that now!")
        return
    
    if isinstance(myitem, Tonic):
        recip = sigmund
    else:
        recip = enemy
    myitem.use(recip)
    del sigmund.supplies[itemchoice]



camp()
