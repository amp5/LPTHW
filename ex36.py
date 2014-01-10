from sys import exit

def kitchen():
    print "You've made it to the kitchen! But wait, how did mom get here?!?!"
    print "How do you get past mom to claim your cookie?"

    next = raw_input(">")
    if next == "hit her":
        dead("That isn't very nice.")

    elif next == "lunge left":
        dead("She lunged left too!")

    elif next == "lunge right":
        dead("She lunged right too!")

    elif next == "tell her dad broke something in the garage":
        print "You are a genius!"
        print "Take your cookie and enjoy the sweet taste of victory!"
    else:
        print "I'm sorry, run that by me one more time."

def hallway():
    print "Ok great! You've taken the first step!"
    print "You see the stairs leading down to the kitchen at the end of the hallway..."
    print "You start walking over but then spot, the dog, comes running up to you, blocking your path."
    print "What do you do?"
    spot_moved = False

    while True:
        next = raw_input("> ")

        if next == "push spot to the side":
            dead("Spot sits on you. You can't move.")
        elif next == "grab tennis ball" and not spot_moved:
            print "Spot got excited!"
            spot_moved = True
        elif next == "throw ball" and spot_moved:
            print "Spot goes chasing after the ball."
            print "Your path has cleared"
            print "You head downstairs"
            kitchen()
        else:
            print "I'm sorry, run that by me again?"

def dead(why):
    print why, "Try again later :( "
    exit (0)

def start():
    print "You are in your bedroom watching TV."
    print "And for some reason an unsatiable desire runs over you - you want a cookie."
    print "Problem is, the cookies are downstairs in the kitchen,"
    print "And it is a lot of effort to go get a cookie"
    print "So what will you do?"

    next = raw_input(">")

    if next == "get up":
        hallway()
    else:
        dead("You lazy. No cookie for you. EVER!")

start()
