print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
    print "Do you want to continue on your adventure?"

    continu = raw_input ("> ")

    if continu == "yes":
        print "Great! Now follow that bear."
        print "So you followed that bear into a set of caves and now you are at a crossroads."
        print "Do you go right or left?"
        direction = raw_input("> ")

        if direction == "right":
            print "You found a pot of gold! Good Job!"
        elif direction == "left":
            print "Uh-oh, you found the bear and his friend, Cthuhlu!"
            print "And now you die. Goodbye!"
    elif continu == "no":
        print "Well fine then! The adventure didn't want to play anyways!"     

elif door == "2":
    print "You stare into the endless abyss at Cthuhlu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "You stumble around and fall on a knife and die. Good job!"

# key point is that I am now putting if-statements inside if-statements as code that
#can run. Powerful. Can be used to create "nested" decisions        
