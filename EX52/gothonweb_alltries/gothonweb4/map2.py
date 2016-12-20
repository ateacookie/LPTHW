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
"""This is the first room. One door to your left and one to your right. (Try the left one first, just to see what happens)

You can do:
go right
go left

To check your inventory you can always type: inventory

""")

left_room = Scene("Left Room", "left_room",
"""This is the left room. In the center lies some Gold! On the other side is another door.

You can do:
go back
pick up gold
go ahead

""")

right_room = Scene("Right Room", "right_room",
"""This is the right room. On the floor lies a big key.

You can do:
go back
pick up key

""")

outside = Scene("Outside", "win",
"""You find yourself outside. Happy to see the sun and be some gold richer! :)

""")



#here are som important things now:

#the arrays are build like that:
#
#1 place: what to do!    0 = do something     1 = go somewhere
#if 0(do something):
#what happens, what is put into your inventory, what gets removed from your inventory

#if 1(go somewhere):
#the next scene, What I need somthing to get there(like a key), what is displayed when I don't have that thing
#

#
starting_point.add_paths({
    'go left': [1, left_room, "key1", "The door is locked! You need a key to enter!"],
    'go right': [1, right_room, None],
    '*': [starting_point, None]
})

right_room.add_paths({
    'go back': [1, starting_point, None],
	'pick up key': [0, "You pick up an old big key and it is added to your inventory", "key1", None] ,
    '*': [1, right_room, None]
})

left_room.add_paths({
    'go back': [1, starting_point, None],
	'pick up gold': [0, "You pick up some Gold", "gold", None, None] ,
	'go ahead': [1, outside, None],
    '*': [1, left_room, None]
})


SCENES = {
    starting_point.urlname: starting_point,
    left_room.urlname: left_room,
    right_room.urlname: right_room,
	outside.urlname: outside
}
START = starting_point
