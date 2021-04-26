class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
   
    pass

dad = Parent()
son = Child()


dad.implicit()
son.implicit()
#对孩子采取的行动意味着对父母采取的行动