# import arguments from sys
from sys import argv


#when we run this file we will
#need to not only call out the script name
#(ex16.py) but also the filename (text.txt)
#we want to create

script, filename = argv


#prints this line, and added into the phrase
#the name of the filename we chose earlier

print "We're going to erase %r." % filename

#print a phrase
print "If you don't want that, hit CTRL-C (^C)."
#print a phrase

print "If you do want that, hit RETURN."


#tells program that whatever user imputs 
#next will be stored as a rawinput
#prompts user to imput something

raw_input("?")


#print statement

print "Opening the file..."
#defines a variable (target)as opening the 
#file we defined when we initiated the program
#opens file in 'write' mode

target = open(filename, 'w')


#prints phrase

print "Truncating the file. Goodbye!"
#variable (target) as defined earlier
#telling program to truncate/empty file

target.truncate()


#print phrase

print "Now I'm going to ask you for three lines."


#asks user to imput three new lines of text.
#each line is entered in as a separate string

line1 = raw_input("line 1: ")

line2 = raw_input("line 2: ")

line3 = raw_input("line 3: ")


#prints phrases

print "I'm going to write these to the file."


#variable defined as the new filename we created
#give the command to write whatever user enters in
#for line 1

target.write(line1)
#tells program to write on a new line in the text.txt file

target.write("\n")
#enters in raw_input from line 2 variable in ex16.py file 
#into line 2 of text.txt

target.write(line2)

#in text.txt file, enters new line
target.write("\n")
#enters in raw_input form line 3 varibale in ex16.py file
#into line 3 of text.txt file

target.write(line3)
#in text.txt file, enters new line

target.write("\n")


#prints phrase

print "And finally, we close it."
#gives close command to variable 'target'
#which is the file I created (text.txt)

target.close()
