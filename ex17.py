from sys import argv

from os.path import exists



script, from_file, to_file = argv



print "Copying from %s to %s" % (from_file, to_file)



#we could do these two on one line too, now?

input = open(from_file)

indata = input.read()



print "The input file is %d bytes long" % len(indata)



print "Does the output file exist? %r" % exists(to_file)

print "Ready, hit RETIRN to continue, CTRL-C to abort."

raw_input()



output = open(to_file, 'w')

output.write(indata)



print "Alright, all done."



output.close()

input.close()



#From here on out I will be putting my notes below

#Instead of going line by line...



#Things I need to note: In command line

#I will type in the name of this file (ex17.py)

#test.txt as the from_file

#and copied.txt as the to_file



#when we import the 'exists' command it returns a True if a file exists, based on it's name in a string as an argument. False, if not. 





#Questions to answer late:

#what does len(indata) mean?
