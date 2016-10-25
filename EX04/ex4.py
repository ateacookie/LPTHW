#cars equals 100
cars = 100
#there are 4 seats in the car, space_in_a_car equals 4.0
space_in_a_car = 4.0
#there are 30 drivers, the number of drivers equals 30
drivers = 30
#there are 90 passengers. the number of passengers equals 90
passengers = 90
#the number of cars that aren't driven is equal to the cars available minus the number of drivers
cars_not_driven = cars - drivers
#the number of driven cars is equal to the number of drivers
cars_driven = drivers
#the capacity of carpool is the number of driven cars times the space in a car
carpool_capacity = cars_driven * space_in_a_car
#the average passengers per car are all passengers divided by the number of driven cars
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car,"in each car."
