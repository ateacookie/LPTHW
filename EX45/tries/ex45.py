# super cool game
from sys import exit
from random import randint

# I N V E N T O R Y
bag = ["flashlight", "rope", "water gun", "floor plan", "snickers"]

class Game(object):

    def start(self,start_room):
        self.game = start_room
        player = raw_input("Please enter username: > ")
        print "Hello %s!" % player
        print "Welcome to "'\033[92m'+"The Adventures of The Hood!"+'\033[0m' #print Title in Green
        print "As you probably know, Robin Hood is the savior of the poor."
        print "He takes from the rich and gives to the poor. And this is exactly what you're"
        print "going to do tonight, %s" % player
        print "Do you feel mentally prepared for your task?" #ready to rumble?
        choice = raw_input("> ")
        if "yes" in choice: #go to foyer
            print "Alright, %s! Let's do this!" % player
            print "Maybe you already noticed that you are carrying a bag."
            print "This is where you put all the valuable things you can find"
            print "in this castle."
            check = raw_input("Check what's inside? > ")
            if "yes" in check:
                print "Your bag contains: "
                print bag
                print "Okay, let's start now."
                self.castle = Foyer()
            else:
                self.castle = Foyer()

        else: #exit game?
            print "Are you sure, you want to exit this game?"
            leave = raw_input("> ")
            if "yes" in leave: #exit
                exit()
            elif "no" in leave:
                print "Do you feel mentally prepared for your task?"
                choice = raw_input("> ")
                if "yes" in choice: #go to foyer
                    print "Alright, %s! Let's do this!" % player
                    print "Maybe you already noticed that you are carrying a bag."
                    print "This is where you put all the valuable things you can find"
                    print "in this castle."
                    check = raw_input("Check what's inside? > ")
                    if "yes" in check:
                        print "Your bag contains: "
                        print bag
                        print "Okay, let's start now."
                        self.castle = Foyer()
                    else:
                        self.castle = Foyer()
                else:
                    print "Well, I don't think you are ready for this."
                    print "Goodbye %s, maybe next time!" % player
                    exit()
# DO I NEED THIS?
# def __init__(self, scene_map): # scene_map = plan of all rooms in castle
#        self.map = scene_map
class Castle(object):

    noise = randint(1,10)
    def make_noise():
        print "That was loud, man!"
        print "You triggered the alarm system."
        print "Run for your life, %s, or face the rest of your life spend in jail." % player
        print "It was nice having you here, though."
        exit()

    if noise == 7:
        make_noise()


class Foyer(Castle):
    def foyer():
        print "You are in the foyer of the castle."
        print "In front of you are stairs, up and down."
        print "To your left you find the kitchen, to your right the dining room."
    foyer()

class Kitchen(Castle):
    pass

class stairs(Castle):
    pass

class stairs_up_1(stairs): #from from dungeon to foyer
    pass

class stairs_up_2(stairs): #from foyer to floor 1
    pass

class stairs_up_3(stairs): #from floor 1 to floor 2
    pass

class stairs_down_1(stairs): #from floor 2 to floor 1
    pass

class stairs_down_2(stairs): #from floor 1 to foyer
    pass

class stairs_down_3(stairs): #from foyer to dungeon
    pass

class Dining_Room(Castle):
    pass

class Library(Castle):
    pass

class secret_room(Castle):
    pass

class Bedroom(Castle):
    pass

class Dungeon(Castle):
    pass

class Casino(Castle):
    pass


# Start the game
game = Game()
game.start(Game)
