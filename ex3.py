# will print out the statement "I willl now count my chickens:"

print "I will now count my chickens:"



#will print how many hens there are: add 25 + (30/6). Seems to follow PEMDAS format

print "Hens", 25.0 +30.0 / 6.0

#will print how many roosters there are:100 - ((25*3)modulo 4 ). To calculate modulo you do x/y. subtract whole number to get only the decimal remainder. times remainder by y to get modulo. In this instance 75%4 is 18.75. .75 * 4 = 3 

print "Roosters", 100.0 - 25.0 * 3.0 % 4.0



#tells us what the next few lines will convey to us.

print "Now I will count the eggs:"



# 3 + 2 + 1 - 5 + (4%2) - (1/4) + 6. Should give us 1 + 0 - 0 + 6. here fractions equal 0. Python 2 doesn't return floats but python 3 does.

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0



#setting up the next line which will evaluate the statement "Is it true that 3 + 2 < 5 - 7"

print "Is it true that 3.0 + 2.0 < 5.0 - 7.0?"



# tells us that 5 < -2. which is false

print 3.0 + 2.0 < 5.0 - 7.0



# tells us that 3 + 2 is 5

print "what is 3.0 + 2.0?", 3.0 + 2.0

# tells us that 5 - 7 is -2

print "What is 5.0 - 7.0?", 5.0 - 7.0

# more words explaining what we have already discovered... it's False

print "Oh, that's why it's False."

# gearing up to show us more examples

print "How about some more."

# shows us that five is greater than negative two

print "Is it greater?", 5.0 > -2.0

#shows us that five is greater or equal to -2

print "Is it greater or equal?", 5.0 >= -2.0

# shows us that 5 is not less than or equal to negative two

print "Is it less or equal?", 5.0 <= -2.0
