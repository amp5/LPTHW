# prints the first question, 
print "How old are you?",
#followed by a space that allows you to enter 
#in information striaght into the command line.
age = raw_input()
#prints the second question
print "How tall are you?",
#followed by a place on the same line
#for you to enter in information into the command line
height = raw_input()
#prints third question
print "How much do you weigh?",
#followed by a place to enter in info into the same command line
weight = raw_input()

#prints a string that aggregates all of the 
#inputs previously entered in by self
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#below is roughly the same thing as above.
#only with carefully crafted follow-up questions
#to learn more about you.
print "Let's find out some more about you?"
print "What is your favorite color?",
color = raw_input()
print "And what is your favorite food?"
food = raw_input()
print """
Lastly, if you were stranded on an island 
and you could pick only three things to have
with you on the island, what would they be.
(people are ok to choose - even though they are not
things)
"""
things = raw_input(), raw_input(), raw_input()

print """
So let me get this straight, 
you like %r, %r, and would choose
%r to take with you on a deserted island.
.....

I see.

That is all.
""" % (color, food, things)
