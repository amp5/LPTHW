def infinite_numbers(ceiling, increment):  

    i = 0
    numbers = []

    print "----------"
    while i < ceiling:
        print "At the top i is %d" % i
        numbers.append(i)

        increment = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "----------"
    print "The numbers: "

    for num in numbers:
        print num

def finite_numbers(ceiling, increment):
    numbers = []

    print "----------"
    for x in range(0, ceiling, increment):
        print "At the top x is %d" %x
        numbers.append(x)

        print "Numbers now: ", numbers
        print "At the bottom x is %d" % (x+increment)

    print "----------"
    print "The numbers:"

    for num in numbers:
        print num

print"What's the largest number you want to reach?"
max_number = int(raw_input("-->"))
print "How do you want to increment it?"
incr = int(raw_input("--> "))

print "*****RUNNING infinite_numbers()*****"
infinite_numbers(max_number, incr) #should block out this line to see if second function works. ctr + c to exit program
print "************************************"

print "***** RUNNING finite_numbers()******"
finite_numbers(max_number, incr)
print "************************************"
