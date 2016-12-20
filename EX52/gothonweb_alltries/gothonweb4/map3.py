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


starting_point = Scene("Start Room", "starting_point",
"""
Hello!
Welcome to The Adventures of The Hood!
As you probably know, Robin Hood is the savior of the poor. He takes from the rich and gives
to the poor.
Tonight he enters a rich man's castle.

It's your task to walk around and collect some valuable stuff.
But be careful: A guard and a watch-dog are lie in a wait.

Your options to act will be shown in each scene.

OPTIONS:
A: enter castle
B: go home

+++ To check what's in your bag, type: bag +++
""")

lobby = Scene("Lobby", "lobby",
"""
You entered the castle and are now in the lobby.
You can hear the guard approaching. How do you want to fight him?

OPTIONS:
A: throw a vase at him
B: go ahead

""")

dining_room = Scene("Dining Room", "dining_room",
"""
You are now in the Dining Room.
If I were you, I would try to collect some valuable stuff now!
Look around! There's a pretty painting, antique dishware and even a bust
of Julius Caesar!

OPTIONS:
A: take pretty painting
B: take antique dishware
C: take bust of Julius Caesar
D: go ahead
E: go back

""")

Library = Scene("Library", "library",
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
A: throw books
B: capitulate
C: go back

""")

SecretRoom = Scene("Secret Room", "secret_room",
"""

""")

finished = Scene("Finished", "win",
"""You find yourself outside. Happy to see the sun and be some gold richer! :)

""")

go_home = Scene("Go home", "go_home",
"""
Bye, loser.
""")

#here are some important things now:

#the arrays are build like that:
#
#1 place: what to do!    0 = do something     1 = go somewhere
#if 0(do something):
#what happens, what is put into your inventory, what gets removed from your inventory

#if 1(go somewhere):
#the next scene, What I need somthing to get there(like a key), what is displayed when I don't have that thing
#


starting_point.add_paths({
    'enter castle': [1, lobby, None],
    'go home': [1, go_home, None],
    '*': [starting_point, None]
})

lobby.add_paths({
    'throw vase': [0, "You threw a vase at the guard and hit his head. You got a little time back-up", None],
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
    'throw books': [0, "As you took one book out, a secret door opens", None],
    'capitulate': [0, "H", None],
    'go back': []

})

# right_room.add_paths({
#     'go back': [1, starting_point, None],
# 	'pick up key': [0, "You pick up an old big key and it is added to your inventory", "key1", None] ,
#     '*': [1, right_room, None]
# })
#
# left_room.add_paths({
#     'go back': [1, starting_point, None],
# 	'pick up gold': [0, "You pick up some Gold", "gold", None, None] ,
# 	'go ahead': [1, outside, None],
#     '*': [1, left_room, None]
# })


SCENES = {
    starting_point.urlname: starting_point,
    lobby.urlname: lobby,
    dining_room.urlname: dining_room,
    library.urlname: library,
    #left_room.urlname: left_room,
    #right_room.urlname: right_room,
	outside.urlname: outside
}
START = starting_point
