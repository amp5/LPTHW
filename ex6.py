# defning x. Also putting a string within a string. 1
x = "There are %d types of people." % 10
#defining binary
binary = "binary"
# defining do_not
do_not = "don't"
#the end of the not hilarious joke. Here there are two strings within this string. 2.3.
y = "Those who know %s and those who %s." % (binary, do_not)

#showing us "There are 10 types of people" statement
print x
# showing us "Those who know binary and whose who don't"
print y

#showing us "I said:..." along with what was in variable x. string within a string. 4.
print "I said: %r." % x
#showing us "I also said:..." along with what was in variable y. string within a string. 5.
print "I also said: '%s'." % y

#defining that the variable hilarious is false
hilarious = False
#defining variable of joke_evaluation as a string of words followed by another string. string within a string 5.5? or 6
joke_evaluation = "Isn't that joke so funny?! %r"

#showing us the equation where "Isn't that joke funny?! False" will show up
print joke_evaluation % hilarious

# defining two variables
w = "This is the left side of ..." 
e = " a string with a right side."
# showing us that we can print out two variable together on one line.
print w + e
