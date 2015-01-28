## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal 
class Dog(Animal):

	def __init__(self, name):
		## dog has-a name?
		self.name = name

## Cat is-a Animal 
class Cat(Animal):

	def __init__(self, name):
		## cat has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		##Employee has-a attributes like name and salary
		##That's how you can run the __init__ method of a parent class reliably.
		super(Employee, self).__init__(name)
		## IDK?? Same as last comment, Emplotee has-a salary?
		self.salary = salary

## Fish is-a object?
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-s Fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat LOL
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet which is-a cat named satan
mary.pet = satan

## frank is-a employee and has-a name of frank and a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet and the pet is-a dog and has-a name of rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

##crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()



