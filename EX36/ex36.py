from sys import exit

def cybermen_room():
    print "You enter Door 1."
    print "This room is full of cybermen who want to implant earpods to you."
    print "Behind the cybermen is a hallway, but you don't know where it leads."
    print "What are you doing?"

    choice = raw_input("> ")
    if "leave" in choice:
        start("So, here you are again. Where do you go now?")
    elif "leave" not in choice:
        second_hallway("Where is this hallway leading you?")
    else:
        dead("Congrats! You've been upgraded!")

def second_hallway(text):
    print "You managed your way out of the cybermen room!"
    print "Now, you are walking along another hallway."
    print "At the end of this hallway you find an Ood."
    ood()

def dalek_room(text):
    print "You entered door 2. But what is this?"
    print "... why does it have a plunger thingy arm?"
    print "Must be one of those Daleks."
    print "'EXTERMINATE!!' 'EXTERMINATE!!'"
    print "You can see Captain Jack's vortex manipulator in one corner."
    vortex_manipulator = False

    while True:
        choice = raw_input("> ")

        if choice == "leave":
            dead("No exit here. Dalek killed you.")
        elif "take" or "vortex manipulator" in choice and not vortex_manipulator:
            print "You managed to get Captain Jack's vortex manipulator. Now use it or run!"
            print "Great! The vortex manipulator directly brought you to the TARDIS!"
            vortex_manipulator = True
            tardis("Yay! You found the TARDIS!")
        else:
            dead("Dalek killed you. Sorry!")

def tardis(text):
    print "This blue beauty has been waiting for you."
    print "Oh, the Doctor is already inside!"
    print "Good job!"
    exit()

def hallway():
    print "So you took the dark hallway. Interesting."
    print "After walking a bit, you see a door on the left."
    print "Do you enter the room or keep going?"
    ood1 = False

    while True:
        choice = raw_input("> ")

        if "enter" in choice:
            dalek_room("You entered the Dalek room.")
            print "Damn!"
        elif "going" in choice and not ood1:
            ood("Oh! What creature is that?")
            ood1 = True
        else:
            dead("There's no going back. A stone is falling on your head. You died.")

def ood(text):
    print "This weird looking alien is an Ood. Oods are very friendly and peaceful"
    print "It leads you the way towards the TARDIS."
    print "Congrats! The doctor has been waiting for you!"
    exit()

def dead(why):
    print why, "GAME OVER!"
    exit(0)

def start(text):
    print """ Hello. You are the new companion of the Doctor!
    You wake up on a strange spaceship in the distant future and
    the TARDIS along with the Doctor has vanished.
    There's only one thing you can do: GO AND FIND THE TARDIS!
    """
    print "Right in front of you you find 2 doors and one dark hallway."
    print "Where do you go?"

    choice = raw_input("> ")

    if choice == "door1":
        cybermen_room()
    elif choice == "door2":
        dalek_room("")
    elif choice == "hallway":
        hallway()
    else:
        dead("While waiting for the Doctor to find you, you're killed by the Silence.")


start("Ah, it's you!")
