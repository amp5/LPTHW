#The variables in your function are not connected to the variables in your script.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#Ergo, you define the function in the beginning, and it acts as a template
#if you will and each time you define the varibles, or tell us how many
#cheeses and crackers we have, it prints out the same function format 
#with the new variables

def money_and_jobs(money_count, job_count):
    print "You have %d dollars" % money_count
    print "You have %d jobs" % job_count
    print "Uh-oh, looks like you are running out of money."
    print "Time to get another job. \n"

print "Let's look at how much money you have and how many jobs you have."
money_and_jobs (1000, 1)

print "Let's try that again."
bank_account = 1500
jobs_current = 2

money_and_jobs(bank_account, jobs_current)

print "What if your parents gave you money?"
money_and_jobs(bank_account + 2000, jobs_current - 1)
