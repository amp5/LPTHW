# defines variable "tabby_cat" as a string of words tabbed to the right.
tabby_cat = "\tI'm tabbed in."
#defines variable "persian_cat" as a string of words split where we see the "\n". 
#The result is that everything after "\n" is now printed on a new line.
persian_cat = "I'm split \non a line."
#defines variable "backslash_cat" as a string with two \'s surrounding the letter "a"
backslash_cat = "I'm \\ a \\ cat."

#defines variable "fat_cat" as a string of letters. Here it is a list of things. 
#after stating that this is a list, each bullet of the list will be printed on a new line 
#and tabbed to the right
# everything in between """ and """ will be part of the formula that "fat_cat" equals.
# using ''' and ''' also does the same thing.
# using """ or ''' is based on style. But for now I will use ''' (it's easier to type anyways)

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

#prints all of the variables we defined above.
#when I add in %r into these print formulas the \t and \\ don't work.
#when I add in %s into these print formulas they work. 
print "This is tabby_cat: %s" % tabby_cat
print "This is persian_cat: %s" % persian_cat
print "This is backslash_cat: %s" % backslash_cat
print "This is fat_cat: %s" % fat_cat
