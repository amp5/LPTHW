#fetching argv from sys
from sys import argv

#defining two arguments, script and user_name
#which you will have to set these parameters as you call out the script
#in the command line
script, user_name, level_experience = argv
#defining the variable 'prompt' to use later
prompt = 'enter information here'

#printing first string, and calling in two arguments defined earlier
print "Hi %s, I'm the %s script." % (user_name, script)
#printing a script which will lead you to the next script
print "I'd like to ask you a few questions."
#Asks user a question, pulling in first second argument
print "Do you like me %s?" % user_name
#asks for raw input from user, using variable 'prompt'
likes = raw_input(prompt)

#prints string calling in second argument
print "Where do you live %s?" % user_name
#asks for raw input, using variable 'prompt'
lives = raw_input(prompt)

#prints string calling in second argument
print "What kind of computer do you have?"
#asks for raw input, using variable 'prompt'
computer = raw_input(prompt)

print "So you are at %s level of experience, right?" % level_experience
experience = raw_input(prompt)


#prints multi-line string, aggregating above-entered raw inputs
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Lastly, your level of experience is %r. Not bad.
""" % (likes, lives, computer, experience)
