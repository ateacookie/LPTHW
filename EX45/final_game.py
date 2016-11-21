from sys import exit
from random import randint

# I N V E N T O R Y
bag = ["flashlight", "rope", "water gun", "floor plan", "snickers"]

class Scene(object):

    def enter(self):
        print "..."
        exit(1)


class Game(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter

class Caught(Scene):

    bye = [
            "At least you tried.",
            "Maybe next time.",
            "Goodbye, my almost lover, Goodbye, my hopeless dream. jk, LOSER!"
    ]

    def enter(self):
        print Caught.bye[randint(0, len(self.bye)-1)]
        exit(1)

class Lobby(Scene):

    def enter(self):
        print "Hello %s!" % player
        print "Welcome to "'\033[92m'+"The Adventures of The Hood!"+'\033[0m' #print Title in Green
        print "As you probably know, Robin Hood is the savior of the poor."
        print "He takes from the rich and gives to the poor. Sadly, he got caught"
        print "the last time when he enterd this castle and has been locked up in"
        print "the castle's dungeon. But today, he managed to escape from his cell"
        print "and is now on the lam."
        print "This is where you're coming into play. You try to take a few valuable"
        print "things from the castle, but be aware of the jail guard and his three"
        print "furious dogs who are chasing you."
        print "And this is exactly what you're going to do tonight, %s" % player
        print "\n"
        print "You're running upstairs and right into the looby of the castle."
        print "You can hear the guard approaching."
        print "How do you want to fight him?"
        print "You can either have a look in your bag, throw a vase at him or fight with"
        print "your own power."

        choice = raw_input("> ")

        if "bag" in choice or "look" in choice:
            print bag
            print "Take something out of your bag?"
            take = raw_input("> ")
            if "water gun" in take:
                bag.remove("water gun")
                print "You shot him right in the eye."
                print "The guard takes a while to re-orientate and you can keep running."
                return 'dining_room'
            elif "snickers" in take:
                bag.remove("snickers")
                print "You offer him a snickers, saying:"
                print "'Eat a snickers. You are not you when you're hungry.'"
                print "He takes it happily. You made a new friend."
                exit()
            else:
                print "You do not get your item out fast enough."
                print "The guard catches you."
                return 'caught'

        elif "throw" in choice or "vase" in choice:
            print "You throw the vase at the guard."
            chance = randint(1,2)
            if chance == 1:
                print "The vase hit the guard's head. He's fallen over and bleeding."
                print "You can keep running."
                return 'dining_room'
            elif chance == 2:
                print "You are a bad thrower."
                print "Shame on you!"
                print "The guard is even angrier and catches you."
                return 'caught'

        elif "fight" in choice or "own" in choice or "power" in choice:
            print "You try to fight with the guard."
            print "Sadly, the guard is a wrestling champion and you're knocked out"
            print "after a view seconds."
            return 'caught'

        else:
            "error 8937: computer cannot read."
            return 'lobby'

class DiningRoom(Scene):



    def enter(self):
        print "That was close!"
        print "So you got rid of the guard, but only God knows for how long."
        print "If I were you, I would try to collect some valuable stuff NOW!"
        print "Look around!"
        print "There's a pretty painting, antique dishware, a golden chandelier"
        print "and even a bust of Julius Caesar!"
        print "wow, crazy stuff."
        print "You better hurry up, if you want to take anything!"
        chance = randint(1,5)
        if chance == 1:
            print "You're too slow! The dogs are surrounding you."
            return 'caught'
        else:
            print "Choose one of the items to add to your bag."
            print "(Don't worry. It's a magical bag. There's even room for an elephant.)"
            take = raw_input("> ")
            if "painting" in take:
                bag.append("pretty painting")
                print "You put the painting in your bag! YAY!"
                print "But you better leave the dining room as fast as you can."
                return 'library'
            elif "antique" in take or "dish" in take:
                bag.append("antique dishware")
                print "You put the antique dishware in your bag! YAY!"
                print "But you better leave the dining room as fast as you can."
                return 'library'
            elif "golden" in take or "chandelier" in take:
                bag.append("golden chandelier")
                print "You put the chandelier in your bag! YAY!"
                print "But you better leave the dining room as fast as you can."
                return 'library'
            elif "bust" in take or "Caesar" in take:
                bag.append("bust of Julius Caesar")
                print "You put the bust in your bag! YAY!"
                print "But you better leave the dining room as fast as you can."
                return 'library'
            else:
                print "No. The item you chose does not exist."
                print "But doesn't matter, the guard is behind you."
                print "Sorry, %s" % player
                return 'caught'

class Library(Scene):

    def enter(self):
        print "You entered the huge library of the castle."
        print "All you can see are shelves filled with books, books and books."
        print "You're hiding behind a shelf."
        print "The guard called for back-up. Now there are 1 guard, 1 cop and 3 dogs"
        print "chasing you."
        print "You look into your bag to see if you got anything useful to defend yourself."
        print bag
        print "Nope, there's nothing useful in there."
        print "\n"

        print "You start grabbing books out of the shelves to build a wall around you."
        print "When the guard and the others come, you just throw books at them,"
        print "because you know: Words can hurt more than actions!"

        keybook = randint(1,10)
        if keybook == 1 or keybook == 5 or keybook == 10:
            print "What's happening?"
            print "The shelf is turning and a secret door opens."
            print "You take your opportunity and walk inside this room."
            print "The shelf is turning again and the door is closed."
            return 'secret_room'
        else:
            print "The guard and the cop are very close."
            print "You decide to throw some books."
            print "\n"
            print "What a pitty! They are wearing book-proof vests."
            print "They grab you and carry you right back into the dungeon."
            print "But this time you are chained to the wall, so you won't"
            print "escape another time."
            return 'caught'


class SecretRoom(Scene):
#    import game45_import

    def enter(self):
        print "That was strange. Just like in a movie!"
        print "This room is very dark, so you better get your flashlight."
        flashlight = raw_input("> ")
        if "get" in flashlight or "flash" in flashlight or "bag" in flashlight:
            print bag
            bag.remove("flashlight")
            print "You turn on the flashlight and see where you are: "
            print "you are in the castle's" '\033[4m'+"treasure romm!"+'\033[0m'
            print "\n"
            print "Everywhere around you are:"
            print "Wow, so many coins, gold bars, bills and money bags!!"
            print "You collect everything and put it into your bag."
            bag.append("coins", "gold bars", "bills", "money bags")
            print "You can leave the room via a slide in the right corner."
            print "Bye, %s!" % player
            return 'finished'

        else:
            print "Why don't you take that f***ing flashlight?"
            print "You can't see anything. Better take it."
            flashlight = raw_input("> ")
            if "get" in flashlight or "flash" in flashlight or "bag" in flashlight:
                print bag
                bag.remove("flashlight")
                print "You turn on the flashlight and see where you are: "
                print "you are in the castle's" '\033[4m'+"treasure room!"+'\033[0m'
                print "\n"
                print "Everywhere around you are:"
                print treasure
                print "You collect everything and put it into your bag."
                bag.append("coins", "gold bars", "bills", "money bags")
                print "You can leave the room via a slide in the right corner."
                print "Bye, %s!" % player
                return 'finished'

            else:
                print "Okay, what's wrong with you?"
                exit()

class Finished(Scene):

    def enter(self):
        print "You managed your way through the castle and even got out with a bag"
        print "full of stuff that you can give to the poor."
        print "Look into your bag! You collected:"
        print bag
        print "Congrats! You won!"
        return 'finished'

class Map(object):

    scenes = {
        'lobby': Lobby(),
        'dining_room': DiningRoom(),
        'library': Library(),
        'secret_room': SecretRoom(),
        'caught': Caught(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


player = raw_input("Please enter username: > ")

a_map = Map('lobby')
a_game = Game(a_map)
a_game.play()
