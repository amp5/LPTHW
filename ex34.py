print "Let's play guess the animal in the list! The game should be pretty straight forward, I will ask you a question about the animals position in the list and you will give me the animal  name."

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
go = raw_input("Ready to proceed? ->")

if go == 'Yes' or go == "yes" or go == "y":

    print animals
    print "The animal at 1?"
    animal = raw_input("-> ")
    while animal != animals[1]:
        print "Incorect. Try again!"
        animal = raw_input("->")
    else:
        print "Correct, the animel is %s.\n" % animals[1]

    print animals
    print "The 3rd animal?"
    animal = raw_input("->")
    while animal != animals[2]:
        print "Incorrect. Try again!"
        animal = raw_input("->")
    else:
        print "Correct, the animal is %s.\n" % animals[2]

    print animals
    print "The 1st animal?"
    animal = raw_input("->")
    while animal != animals[0]:
        print "Incorrect. Try again!"
        animal = raw_input("->")
    else:
        print "Correct, the animal is %s.\n" % animals[0]

    print animals
    print "The animal at 3?"
    animal = raw_input("->")
    while animal != animals[3]:
        print "Incorrect. Try again!"
        animal = raw_input("->")
    else:
        print "Correct, the animal is %s.\n" % animals[3]

    print animals
    print "The 5th animal?"
    animal = raw_input("->")
    while animal != animals[4]:
        print "Incorrect. Try again!"
        animal = raw_input("->")
    else:
        print "Correct, the animal is %s.\n" % animals[4]

    print animals
    print "The animal at 2?"
    animal = raw_input("->")
    while animal != animals[2]:
        print "Incorrect. Try again!"
        animal = raw_input("->")
    else:
        print "Correct, the animal is %s.\n" % animals[2]

    print animals
    print "The 6th animal?"
    animal = raw_input("->")
    while animal != animals[5]:
        print "Incorrect. Try again!"
        animal = raw_input("->")
    else:
        print "Correct, the animal is %s.\n" % animals[5]

    print animals
    print "The animal at 4?"
    animal = raw_input("->")
    while animal != animals[4]:
        print "Incorrect. Try again!"
        animal - raw_input("->")
    else:
        print "Correct, the animal is %s.\n" % animals[4]

    print "We are all done here. Thanks for playing. You've done a great job, keep it up!"         
     

else:
    print "Well I guess you don't want to play this game then! Bye now!"
