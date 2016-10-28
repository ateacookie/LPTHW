#setting the function cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) #assigning numbers in function directly


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#giving numbers from variables

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#"calculating" numbers for function

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#combining all methods to get numbers to the function


print "How much cheese do you have?"
cheese_amount = raw_input()

print "Ok, so you got %r cheeses, right?" % cheese_amount
