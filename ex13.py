#import features(a.k.a modules, or libraries) from Python feature set.
#calling argv - the argument variable which holds the arguments 
#you pass to your Python script when you run it.  
from sys import argv

#line below unpacks argv so it gets assigned to 
#four variables you can work with
#saying that you take whatever is in argv and assign
#it to all of these variables on the left in order
script, first, second, third = argv

#Here I am integrating the raw_input formula with the argv formula
#this way users can enter in data
first = raw_input("What is your first variable")
second = raw_input("What is your second variable")
third = raw_input("What is your third variable")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
 
