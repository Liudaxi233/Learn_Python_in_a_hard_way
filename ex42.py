class Animal(object): #animal is a object
    pass

class Dog(Animal): #dog is a animal
    def _init_(self, name):
        self.name = name

class Cat(Animal): #cat is a animal
    def _init(self, name):
        self.name = name
class Person(object): #person os a object
    def _init_(self, name):
        self.name = name
        self.pet = None
class Employee(Person):   #employee is a person
    def _init_(self, name, salary):
        super(Employee, self)._init_(name)
        self.salary = salary
class Fish(object): #fish is a object
    pass
class Salmon(Fish): #salmon is a fish
    pass
class Halibut(Fish): #halibut is a fish
    pass

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satanfrank = Employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()