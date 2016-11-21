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
