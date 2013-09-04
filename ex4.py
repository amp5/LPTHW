# There are 100 cars. defining the variable cars to equal 100
cars = 100
# There are four spaces in each car.

space_in_a_car = 4.0
# 30 drivers

drivers = 30
#90 passengers

passengers = 90
# telling us that the cars without drivers are the cars in existance not being driven at the moment

cars_not_driven = cars - drivers
#if a car has a driver, then it is being driven

cars_driven = drivers
#the number of seats in a car that is currently being driven. Not including the cars not driven/without drivers

carpool_capacity = cars_driven * space_in_a_car
# taking the number of people in a car (minus the driver?) and dividing that number by the number of cars driven (so drivers)

average_passengers_per_car = passengers / cars_driven


# tells us how many cars there are

print "There are", cars, "cars available."
#tells us how mnay drivers there are

print "There are only", drivers, "drivers available."
#tells us how mnay cars there are without drivers

print "There will be", cars_not_driven, "empty cars today."
# tells us how mnay open seats there are (sans driver seats) for passengers

print "We can transport", carpool_capacity, "people today."
#tells us how many passegers there are

print "We have", passengers, "to carpool today."
# tells us the average of passengers per car

print "We need to put about", average_passengers_per_car, "in each car."
