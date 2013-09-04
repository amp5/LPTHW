# Here's some new strange stuff, remember type it exactly.

#defines variable 'days' as M-Su
days = "Mon Tue Wed Thu Fri Sat Sun"
#defines variable 'months' as Jan-Aug. 
#Also note that instead of separating the right side of the question by spaces
#we can also separate using '\n'. 
#The difference here is that the results are each printed on different lines. 
#the above 'days' were all printed on the same line.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#prints the statement and the variable:
#resulting in showing us the days of the week all on one line
#Note that the exercise shows the statement "Here are the days: " 
#but the 'What you should see section' shows "Here's the days: "
print "Here are the days: ", days
#prints the statement and the variable's results. 
#Each result is printed on its own line. 
print "Here are the months: ", months

#prints the statement below. But by using three double quotes 
#we can use the same command (here it is print) on multiple lines
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6
"""
