from sys import argv #importing module

script, input_file = argv #setting variables

def print_all(f): #setting print_all function, is to read the whole file
    print f.read()

def rewind(f): #setting rewind function
    f.seek(0) #starts at the beginning of file

def print_a_line(line_count, f): #setting print_a_line function
    print line_count, f.readline()

current_file = open(input_file) #current_file = open the file we put into argv

print "First let's print the whole file:\n"

print_all(current_file) #print whole file

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1 #1
print_a_line(current_line, current_file)

current_line += 1 #1+1=2
print_a_line(current_line, current_file)

current_line += 1 #2+1=3
print_a_line(current_line, current_file)
