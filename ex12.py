#defines variables below and will display the script in the command line.
#also allows for user to input raw data
age = raw_input ("How old are you? ")
height = raw_input ("How tall are you? ")
weight = raw_input ("How much do you weigh? ")

#prints the aggregation of all three variables and the inputs
#entered by users
print "So, you're %r old, %r tall, %r heavy." % (
    age, height, weight)
