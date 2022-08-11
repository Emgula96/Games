from time import sleep
import random
import Gfunks

def stars():
    print('**********************************************************')

def death():
    print('Your hp has reached 0')
    print('Garfield unhinges his jaws and the world fades to black')
    sleep(5)
    print('You lose...\n')
    sleep(3)
    playAgain = input('Want to play again? Y/N\n -->')
    while playAgain != 'Y' and playAgain != 'N':
        playAgain = input('Please type "Y" or "N"\n -->')
    if playAgain == 'Y':
        GarfieldLargerThanLife()
    elif playAgain == 'N':
        print('Garfield wickedly waves goodbye')

def GarfieldLargerThanLife():

    class Character:
        def __init__(self,name,health,attack,items):
            self.name = name
            self.health = health
            self.attack = attack
            self.items = items

        def addItmes(self, items):
            self.items.append(items)
            print(f'Your current items are now..{self.items}')

        def printChar(self):
            print(f'Name: {self.name}, Health: {self.health}, Attack: {self.attack}, Items: {self.items}')
        
        def hitByAttack(self, damage):
            self.health -= damage 
            if self.health == 0:
                death()
                exit(0)

        def attackBigBoi(self, foe):
            foe.hitByAttack(self.attack)
            
    def garfieldhit():
        print(f'Garfields new health is {megaCat.health}')

    drawers = ['lighter']
    garItems = ['gasoline']
    def emptyItem(item):
        del item[0]

    megaCat = Character('Garfield', 9000, 50, ['Lasagna'])
    Jon = Character('Jon', 200, 10, ['cigarette'])
    #MAIN MENU
    
    def mainMenu():
        print('\n       Welcome to "GARFIELD: LARGER THAN LIFE" ')
        sleep(3)
        stars()
        print("""
                Main Menu\n
        1. Play
        2. Preface
        3. Exit
        """)
        choice = input("Indicate how you wish to proceed by typing in the number you've chosen \n --> ")
        while choice != '1' and choice != '2' and choice !='3':
            choice = input('Please choose a number 1- 3\n -->')
        if choice == '1':
                gameStart()
        elif choice == '2':
                preface()
        elif choice == '3':
                print('Goodbye' )
    #Preface
    def preface():
        Gfunks.prefaceLog()
        prefaceUser = input('Please enter "B" for back or "Q" to quit \n -->' )
        while prefaceUser != 'B' and prefaceUser != 'Q':
            prefaceUser = input('Please input B or Q \n --> ' )
        if prefaceUser == 'B':
                stars()
                mainMenu()
        if prefaceUser == 'Q':
            print("Goodbye" )
            exit(0)
#GAMESTART
    def gameStart():
        print('\nYou are playing as "Jon" your stats are listed below:\n')
        Jon.printChar()
        stars()
        sleep(7)
        print('Your once good buddy Garfield has turned into a monster.')
        sleep(3)
        print("He is hiding somewhere in the house.....be careful.")
        sleep(5)
        print('The lights in the house are continuing to flicker.\n')
        print('Odie has gone missing and you have been locked in your room for protection.')
        sleep(5)
        print('You need to put an end to this nightmare, once and for all.') 
        sleep(5)
        print( "You slowly unlock your door.\n")
        stars()
        chooseRoom()

    def chooseRoom():
        print(''' Where would you like to go?\n
            1. The Kitchen
            2. The Garage  
            3. Outside the house
            4. The Study
            5. Quit''')

        door = input("--> ")
        while door != '1' and door != '2' and door != '3' and door != '4' and door != '5':
            door = input("Please enter a number 1 - 4-->  ")
        if door == '5':
            print('Garfield wickedly waves goodbye')
            exit(0)
        print('You are traveling.....')
        sleep(3)
        randomAttack = random.randint(0,5)
        stars()
        if randomAttack == 1:
            print('Garfield hears you shuffling in between rooms and attacks while you are in transit.')
            sleep(3)
            print('Garfield launches a sneak attack and hurries back into the vents.')
            Jon.hitByAttack(megaCat.attack)
            print(f'Your health is now {Jon.health}')
            sleep(3)
            stars()
        if door == '1':
            kitchen()
        if door == '2':
            garageOptions()
        if door == '3':
            outside()
        if door == '4':
            study(vent)

#KITCHEN
    def kitchen():
        print('You are in the Kitchen.')
        sleep(1.5)
        print('''What do you want do:

            1. Grab the nearby gun
            2. Search the kitchen drawers
            3. Inspect the lasagna pan
            4. Travel to a different room\n''')
            
        stars()
        kitChoice = input('--> ')
        while kitChoice != '1' and kitChoice != '2' and kitChoice != '3' and kitChoice != '4':
            kitChoice = input("Please enter a number 1 - 3 -->  ")
        if kitChoice == "1":
            print('You grab the gun and begin to inspect it. The lights go out.')
            sleep(4)
            print('You look up and see a cat-like silhouette across the room!')
            sleep(4)
            stars()
            print('''Do you?

            1. Shoot it!
            2. Fire a warning shot near the thing''')

            stars()
            gun = input('--> ')
            while gun != '1' and gun != '2':
                gun = input("Please enter a number 1 or 2 -->  ")
            if gun == "1":
                print("The lights come back on, You point the gun and shoot Garfield")
                sleep(2)
                stars()
                print('''\n\n
The bullet demolishes one of Garfield's now 20 eyes. He suddenly appears as a 
15 foot monster with spider legs and a dark shroud fills the room.\n''')
                Jon.attackBigBoi(megaCat)
                garfieldhit()
                sleep(7)
                print('''
Garfield is largely unaffected by the 
bullet and responds in perfect english:''')
                sleep(4)
                print('"Bullets. Wont. Work."\n')
                stars()
                sleep(3)  
                print('Garfield now lunges forward and attacks, causing damage and forcing the gun out of your hand.')
                sleep(3)
                print('Garfield shuffles into the vents')
                Jon.hitByAttack(megaCat.attack)
                print(f'Your health is now {Jon.health}')
                sleep(3)
                print('You run to the garage.')
                sleep(3)
                stars()
                sleep(4)
                garageOptions()
            elif gun == '2':
                print('You fire the warning shot.')
                sleep(3)
                print('The lights come back on, but continue to flicker.')
                sleep(3)
                print('Garfield stares at the new bullet hole in the wall, buying you time to escape.')
                print('You run into the garage and lock the door behind you, you hear garfield climb into the vents.')
                print('You drop the gun in all the commotion.')
                sleep(7)
                stars() #or ask where to flee/travel
                garageOptions()
            else:
                print('Please only type a number 1 - 2')
            
    #KITCHEN 2nd OPTIon
        elif kitChoice == '2':
            if 'lighter' in drawers:
                print(f'You search the drawers and find a {drawers[0]}')
                Jon.addItmes(drawers[0])
                emptyItem(drawers)
            else: print('You search the drawers, but find nothing')
            stars()
            sleep(3)
            kitchen()
    #KITCHEN OPTION 3
        elif kitChoice == '3':
            print('You walk over and peer into the lasagna pan.')
            print('You are overwhelmed by a fowl stench.')
            sleep(3)
            print('You notice some strange remains at the bottom of the pan.')
            print('Every instinct you have is telling you to go back.')
            sleep(3)
            print('''What do you want to do?

            1. Go back
            2. Continue inspecting pan
            ''')
            
            gar3 = input('-->' )
            while gar3 != '1' and gar3 != '2':
                gar3 = input("Please enter a number 1 or 2 -->  ")   
            if gar3 == '1':
                stars()
                kitchen()
            elif gar3 == '2':
                print("You feel a malevolant force push you into the pan.")
                sleep(3)
                print("Garfield now seems to tower over the pan.")
                sleep(3)
                print('He has a wide grin and says "You are the lasagna now, Jon."')
                sleep(3)
                death()
        elif kitChoice == '4':
            chooseRoom()

    #DEATH
    #GAROPTIONS
    def garageOptions():
        print('You are in the Garage.')
        print('''What do you do?
            1. Walk over to the electrical box
            2. Fill a gasoline canister
            3. Inspect the weird bag in the corner
            4. Travel to a new room
        ''')
        stars()
        garChoice = input('--> ')
        while garChoice != '1' and garChoice != '2' and garChoice != '3' and garChoice != '4':
            garChoice = input("Please enter a number 1 - 3 -->  ")
    #GARAGE CHOICE ONE
        if garChoice == "1":
            print(''' 
            You walk over to the electrical box, but notice it doesn't want to open
            Do you:

            1. Go back
            2. Try to pry it open''')
            elect = input('-->')
            while elect != '1' and elect != '2':
                elect = input("Please enter a number 1 or 2 -->  ")
            if elect == '1':
                stars()
                garageOptions()
            elif elect == '2':
                print('''
        While trying to force the box open you accidentally touch some live wires.''')
    #garfield message and say youve opened box
            Jon.hitByAttack(50)
            print(f'Your new health is {Jon.health}')
            print("Something tells you this doesn't want to open...")
            stars()
            garageOptions()
    #GARAGE CHOICE TWO
        elif garChoice == '2':
            if 'gasoline' in garItems:
                print(f'You pour {garItems[0]} into a canister and add it to your items')
                Jon.addItmes('gasoline')
                emptyItem(garItems)
                sleep(3)
                stars()
            else: print('There is no gasoline left')
            garageOptions()#or travel
    #GARAGE  CHOICE THREE
        elif garChoice == '3':
            print('You walk over towards the bag')
            sleep(3)
            print("You find Odie's lifeless body in the bag, attached is a note\n")
            sleep(3)
            print('''You're next Jon....
            
signed, 
        -G''')
            print('The emotional damage of losing Oddie is too much, you lose 50 health')
            Jon.hitByAttack(50)
            print(f'Your new health is {Jon.health}')
            stars()
            garageOptions()

    #GARAGE TRAVEL
        elif garChoice == '4':
            stars()
            chooseRoom()
    #OUTSIDE
    def outside():
        print('You are outside of the house.')
        print('''What do you want to do?\n
        1. Run for it.
        2. End it all.
        3. Search the backyard.
        4. Travel to a new room. 
        \n''')
        stars()
        outChoice = input('-->')
        while outChoice != '1' and outChoice != '2' and outChoice != '3'and outChoice != '4':
            outChoice = input('Please choose one of the above options only.')
        if outChoice == '1':
            print('''As you begin to take your first steps something tells you this isn't right...
\n\nThis isn't how it ends.''')
            sleep(3)
            stars()
            outside()
        elif outChoice == '2':
            if 'cigarette' in Jon.items and 'lighter' in Jon.items and 'gasoline' in Jon.items and 'Important Documents' in Jon.items:
                endItAll()
            else:
                print('You do not have the required materials to end this nightmare.')
                sleep(3)
                print('You must go retrieve more items.')
                sleep(2)
                stars()
                outside()
        elif outChoice == '3':
            print('You search the backyard, and find a key.')
            print('I wonder what it goes to...')
            Jon.addItmes('desk key')
            stars()
            outside()
        elif outChoice == '4':
            stars()
            chooseRoom()
    #ENDITALL
    def endItAll():
        Gfunks.endAlltxt()
        playAgain = input('Want to play again? Y/N\n -->')
        while playAgain != 'Y' and playAgain != 'N':
            playAgain = input('Please type "Y" or "N"\n -->')
        if playAgain == 'Y':
            GarfieldLargerThanLife()
        elif playAgain == 'N':
            print('Garfield wickedly waves goodbye')

    vent = 'open'
    def study(vent):
        print('You have arrived in the Study.')
        print('''What would you like to do?

        1. Inspect your desk
        2. Close the open vent above the desk
        3. Walk over to the bookshelf 
        4. Tavel to a different room
        ''')
        stars()
        studyInput = input('-->')
        while studyInput != '1' and studyInput != '2' and studyInput != '3' and studyInput != '4':
            studyInput = input('Please only enter a number 1 - 4 \n -->')

        if studyInput == '1'and vent == 'open':
            print('You walk over and sit down at your desk')
            print('Oh no you forgot to shut the vent!!!')
            print('Garfield claws you from inside the vent.')
            sleep(3)
            Jon.hitByAttack(megaCat.attack)
            print(f'Your new health is {Jon.health}.')
            print('You shut the vent preventing further onslaught.')
            vent = 'closed'
            sleep(3)
            print('You should try and inspect the desk again.')
            study(vent)
        if studyInput == '1' and vent == 'closed':
            print('You sit down and try to unlock your desk')
            if 'desk key' in Jon.items:
                print('You unlock the desk!')
                sleep(2)
                print('You gather all of your important documents')
                sleep(2)
                print('You now have nothing tying you to this place.')
                sleep(2)
                Jon.addItmes('Important Documents')
                sleep(3)
                stars
                study(vent)
            else: 
                print('You try to unlock the desk but it wont budge.')
                print('You need to go find the key!\n')
                sleep(5)
                stars()
                study(vent)


    #CLOSING VENT
        elif studyInput == '2':
            sleep(3)
            print('You walk over and firmly close the vent.')
            sleep(3)
            print('You feel safer while in this room.')
            sleep(2)
            stars()
            vent = 'closed'
            study(vent)
    # #BOOKSHELF
        elif studyInput == '3':
            print('You walk over to your bookshelf')
            print('One black book catches your eye')
            sleep(4)
            print('You hold the book in your hands and feel an ominous power')
            print('''The title of the book reads:
            
            Conjurings and Summonings of the Occult''')
            sleep(3)
            stars()
            print('''Do you?
            
            1. Open the book
            2. Put it back''')
            book = input('-->')
            while book != '1'and book != '2':
                input('Please open the book or put it back, Id put it back.')
            if book == '1':
                print('You open the book and darkness fills the office')
                print('Out of a portal Garfield is summoned')
                sleep(5)
                stars()
                print('He now stands before you ready for one final fight. ')
                stars()
                print('You and Garfield have a fight to the death')
                print('It doesnt end in your favor.')
                sleep(3)
                death()

            elif book == '2':
                print('You place the book back on the shelf')
                print('I think you made the right choice...')
                sleep(3)
                stars()
                study(vent)

        elif studyInput =='4':
            chooseRoom()

    mainMenu()

#GAME SEQUENCE

GarfieldLargerThanLife()