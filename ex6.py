# x is a variable for ..., %d = 10
x = "There are %d types of people." % 10
# binary is the text binary
binary = "binary"
# do_not is variable for don't
do_not = "don't"
# y is variable for "..." with strings
y = "Those who know %s and those who %s." % (binary, do_not)

# printing x & y meaning the text they stand for
print x
print y

# %r & %s are replaced by what the variable x & y stand for
print "I said %r." % x
print "I also said: '%s'." % y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
