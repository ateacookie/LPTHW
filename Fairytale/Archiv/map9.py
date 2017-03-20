class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}
        self.event = ""

    def do(self, input1):
        #self.event = self.paths.get(input1)[1]

        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')[1]
        return self.paths.get(input1, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)


# GENERAL CODE FOR BOTH GAMES
choose_game = Scene("Choose Game", "choose_game",
"""Welcome!
You got two games to choose from.

[in this case type either 1 or 2]

1: Gothons of Planet Percal #25
2: The Adventures of the Hood
""")

generic_death = Scene("Death...", "death", "You died. You kinda suck at this. Your mom would be proud...if she were smarter.")


# GOTHON GAME
gothon_game = Scene("Gothons of Planet Percal #25", "gothon_game",
"""
Welcome!
You chose Gothons of Planet Percal #25.

Continue?
1. Yes
2. No
""")

central_corridor = Scene("Central Corridor", "central_corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member (oh noes!) and your
last mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow up the ship after getting into an escape pod.

You're now running down the central corridor to the Weapons Armory when a
Gothon hops out in an evil clown costume filled with hate. He's blocking the door
to the Armory and about to pull a weapon to blast you.

OPTIONS:
1. Tell a joke
2. Shoot!
3. Dodge!
""")

laser_weapon_armory = Scene("Laser Weapon Armory", "laser_weapon_armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vg fb sng, jura fur vfvg nebhaq gut ubhfr, fur fvgf nebhaq gut ubhfr.
The Gothon bursts into laughter and rolls around on the ground. While its
laughing you run up and use your copy of Nietzsche's notebooks (translated into Gothon)
to lecture the Gothon on the shaky foundations of its ideologies. While it tries
to cope with its existential crisis, you leap through the Weapon Armory door.

You dive roll into the Weapon Armory, crouch and scan the room for more Gothons
that might be hiding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the neutron bomb in its
container. There's a keypad lock on the box and you need the code to get the bomb
out. The code is 3 digits.

OPTIONS:
1. 587
2. 132
3. 863
""")

the_bridge = Scene("The Bridge", "the_bridge",
"""
The container clicks open and the seal breaks, letting gas out. You grab the
neutron bomb and run like heck to the bridge where you place it in the right spot.

You burst into the Bridge with the bomb under your arm and surprise 5 Gothons
who are trying to take control of the ship. Each of them has an uglier clown costume
that the last. They don't pull their weapons out of fear that they will set off
the bomb under your arm.

OPTIONS:
1. throw the bomb
2. slowly place the bomb
""")

escape_pod = Scene("Escape Pod", "escape_pod",
"""
You gesture towards the bomb and threaten to set it off, the Gothons put up
their arms and ask for a truce. You inch backwards to the door, open it, and
carefully place the bomb on the floor, waving your finger over the detonate button.
Then you jump back through the door, hit the close button and zap the lock so they
can't get out. Now that the bomb is placed you run to the escape pod.

You rush through the ship desperately trying to make it to the escape pod. It seems
like there's no Gothons around, so you run as fast as possible. Eventually you reach
the room with the escape pods, and you now need to pick one to take. Some of them could
be damaged, but you don't have time to look. There's 5 pods, which one do you take?

OPTIONS:
1. 5
2. 4
3. 3
4. 2
5. 1
""")

the_end_winner = Scene("You Made It!", "the_end_winner",
"""
You jump into pod 2 and hit the eject button. The pod flies out into space heading
to the planet below. As you're heading down, you look back and see your ship implode
and then explode like a supernova, taking down the Gothon ship at the same time.
You made it!
""")

the_end_loser = Scene("...", "the_end_loser",
"""
You jump into a random pod and hit the eject button. The pod escapes into space
but there's a crack in the hull. Uh oh. The pod implodes and you with it.
""")


# THE HOOD
the_hood = Scene("Adventures of the Hood", "the_hood",
"""
Welcome!
You chose Adventures of the Hood.

Continue?
1. Yes
2. No
""")

start_hood = Scene("The Hood", "start_hood",
"""
As you probably know, Robin Hood is the savior of the poor. He takes from the rich and gives
to the poor.
Tonight he enters a rich man's castle.

It's your task to walk around and collect some valuable stuff.
But be careful: A guard and a watch-dog are lie in a wait.

Your options to act will be shown in each scene.

OPTIONS:
1. enter castle
2. go home

+++ To check what's in your bag, you can always type: inventory +++
""")

lobby = Scene("Lobby", "lobby",
"""
You entered the castle and are now in the lobby.
You can hear the guard approaching. How do you want to fight him?

OPTIONS:
1. throw a vase at him
2. go ahead
""")

dining_room = Scene("Dining Room", "dining_room",
"""
You are now in the Dining Room.
If I were you, I would try to collect some valuable stuff now!
Look around! There's a pretty painting, antique dishware and even a bust
of Julius Caesar!

OPTIONS:
1. take pretty painting
2. take antique dishware
3. take bust of Julius Caesar
4. go ahead
5. go back
""")

library = Scene("Library", "library",
"""
You entered the huge library of the castle.
All you can see are shelves filled with books, books and books.
You're hiding behind a shelf.
The guard called for back-up. Now there are 1 guard, 2 cops and 3 dogs
chasing you.
You look into your bag to see if you got anything useful to defend yourself.

Nope, there's nothing useful in there.

You start grabbing books out of the shelves to build a wall around you.
When the guard and the others come, you got the following options., you just throw books at them,
because you know: Words can hurt more than actions!

OPTIONS:
1. throw books
2. capitulate
3. go back
""")

secret_room = Scene("Secret Room", "secret_room",
"""
As you pull out the books out of the shelves, a secret door opens to your right.
That's really strange, just like in a movie!
This room is very dark, so you get your flashlight out of your bag.
Now you can see where you are, everywhere around you:
coins, gold bars, bills and money bags!!
You start collecting them and then can leave the room via a slide in the corner.

type: bye
""")

end_hood = Scene("End Hood", "end_hood",
"""
Sorry, you got caught. Better try it another time again.
""")

finished_hood = Scene("Finished Hood", "finished_hood",
"""
Yaay! You managed to escape from the castle with your bag filled to the top.
Congrats!!
""")



# CHOOSE GAME!
choose_game.add_paths({
    '1': [1, gothon_game, None],
    '2': [1, the_hood, None],
    '*': [1, choose_game, None]
})


# GOTHON GAME
gothon_game.add_paths({
    'yes': [1, central_corridor, None],
    'no': [1, choose_game, None]
})

central_corridor.add_paths({
     'shoot!': [1, generic_death, None],
     'dodge!': [1, generic_death, None],
     'tell a joke': [1, laser_weapon_armory, None],
     '*': [1, central_corridor, None]
})

laser_weapon_armory.add_paths({
    '587': [0, "Wrong Code", None],
    '132': [1, the_bridge, None],
    '863': [0, "Wrong Code", None],
    '*': [1, laser_weapon_armory, None]
})

the_bridge.add_paths({
    'throw the bomb': [1, generic_death, None],
    'slowly place the bomb': [1, escape_pod, None],
    '*': [1, the_bridge, None]
})

escape_pod.add_paths({
    '2': [1, the_end_winner, None],
    '*': [1, the_end_loser, None]
})

# THE HOOD
the_hood.add_paths({
    'yes': [1, start_hood, None],
    'no': [1, choose_game, None]
})

start_hood.add_paths({
    'enter castle': [1, lobby, None],
    'go home': [1, choose_game, None]
})

lobby.add_paths({
    'throw a vase him': [0, "You threw a vase at the guard and hit his head. You got a little time back-up", None],
    'go ahead': [1, dining_room, None],
    '*': [1, lobby, None]
})

dining_room.add_paths({
    'take painting': [0, "You took the painting and put it in your bag", "painting", None],
    'take antique dishware': [0, "You put the antique dishware in your bag", "antique dishware", None],
    'take bust': [0, "You took the bust and put it in your bag", "bust of Julius Caesar", None],
    'go ahead': [1, library, None],
    'go back': [1, lobby, None]
})

library.add_paths({
    'throw books': [1, secret_room, None],
    'capitulate': [1, end_hood, None],
    'go back': [1, dining_room, None]
})

secret_room.add_paths({
    'bye': [1, finished_hood, None],
    '*': [1, secret_room]
})



SCENES = {

    choose_game.urlname: choose_game,
    generic_death.urlname: generic_death,

    gothon_game.urlname: gothon_game,
    central_corridor.urlname: central_corridor,
    laser_weapon_armory.urlname: laser_weapon_armory,
    the_bridge.urlname: the_bridge,
    escape_pod.urlname: escape_pod,
    the_end_winner.urlname: the_end_winner,
    the_end_loser.urlname: the_end_loser,

    the_hood.urlname: the_hood,
    start_hood.urlname: start_hood,
    lobby.urlname: lobby,
    dining_room.urlname: dining_room,
    library.urlname: library,
    secret_room.urlname: secret_room,
    end_hood.urlname: end_hood,
    finished_hood.urlname: finished_hood
}

START = choose_game
