def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract (height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

#The character '=' is used to name variables and set them to 
#numbers of strings.
#When you use 'return' with '=', you can set variables to be 
#values from a function
#The extra cradit should be: 
#iq = 100 / 2 = 50
#divide = 50 / 2 = 25
#multiply = 180 * 25 = 4500
#subtract = 74 - 4500 = -4426
# add = 35 + - 4426 = -4391

#Notice that when we are doing our own math functions 
#for 'add' 'subtract', etc., the line 'return a = b' for eaxample
#   our function is called with two arguments: 'a' and 'b'
#   we print out what our function is doing, in this case 'ADDING'
#   then we tell Python to do soemthing kind of backwardm 
#      we return the addition of 'a = b'
#      in English it would be "I add a and b then retun them"
#   Python adds two numbers. Then when the funciton ends any line that
#      runs it will be able to assign this a = b result to a variable

#Some more practice:

def add(a, b):
    print"I'm adding %d + %d now please wait..." % (a, b)
    return a + b

money = add(420, 118)

print "I earned", money, "dollars these past two weeks while I was in NY!" 


# further practice with the extra credit
why = multiply(2, divide(subtract(height, subtract(what, age)), weight))

print "Now I should get", why, "as my result"

#age = 35
#subtract = -4391 - 35 = -4426
#subtract = 74  - -4426 = 4500
#divide = 4500 / 180 = 25
#multiply = 2 * 25 = 50
