#Functions do three things:
# 1. name pieces of code the way variables name strings and numbers
# 2. take arguments the way your scripts take argv
# 3. using #'s 1 and 2, they let you make your own 'tiny commands'
#To create a function, use 'def' in Python


# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

#for the first function
# 1. tell Python we want to make a function using 'def' for define
# 2. same line as 'def', we give the function name (print_two) 
#   your function name should be short and it should say what it does
# 3. next we tell it what we want (*args). Must go inside () to work
# 4. end line with ':' and start indenting
# 5. after colon, all lines indented will become attached to this name
#   'print_two'. first indented line unpacks the arguments
# 6. to demonstrate we then print out the argument

# problem with first function: not the easiest way to make a function
# we can skip the unpacking part and just use the names we waant
# inside the ()
