#imports the module argv from the system
from sys import argv

#sets variable for argv
script, filename = argv

#stets txt to open the file
txt = open(filename)

print "Here's your file %r:" % filename
#opens file
print txt.read()

print "Type the filename again:"
#opens file again because the user types in file name
