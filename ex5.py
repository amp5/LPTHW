name = 'Zed A. Shaw'
age = 35 # not a lie
height_am = 74 # inches
weight_am = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_eu = height_am * 2.54
weight_eu = weight_am / 2.2



print "Let's talk about %s." % name
print "He's %d centimeters tall." % height_eu
print "He's %d kilograms heavy." % weight_eu
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_eu, weight_eu, age + height_eu + weight_eu)
