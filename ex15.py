#import arguments from sys
from sys import argv


#when we run this program we will have to type 
#the script (ex15.py) as well as the file we will
#want to open (ex15_sample)

script, filename = argv


#defining a new variable, txt 
#as the command 'open'
#parameters being the 'filename'

txt = open(filename)


#print line of text and bringing in the variable
#filename as well

print "Here's your file %r:" % filename
#giving the command 'read' with no parameters
#to read the variable 'txt' (= filename)

print txt.read()

txt.close()
#print a line of text

print "I'll also ask you to type it again:"

#defning varible and asking user to input name of file
#syombol that will be displayed here will be '>'

file_again = raw_input("> ")


#defining another variable, which will open whatever
#user entered in above (as the variable file_again)

txt_again = open(file_again)


#will read 'txt_again' anf print what it reads

print txt_again.read()
txt.close()
