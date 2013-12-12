#An if statement creates what is called a 'branch' in the code
#can go in multiple directions (like choose your own adventure games)
#literally - 'if this function is T, then run the code under it.
#if not, skip it.

#code under the if statment needs to be indented 4 spaces because
#a colon at the end of a line if how you tell Python you are going
#to create a new 'block' of code. then indenting 4 spaces tells
#Python what lines of code are in that block

#if the lines under the if statement aren't indented - likely get an error
#python expects you to indent something after you end a line with a :

#you can put other boolena expressions from earlier into an if statement

#if you change the initial variables, different if-statements will 
#evaluate to T and the blocks of code under them will run. 


people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
