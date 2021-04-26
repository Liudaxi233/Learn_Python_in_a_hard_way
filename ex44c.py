class Parent(object):
    def altered(self):
        print("PARENT altered()")
        print("sss")

class Child(Parent):
   def altered(self):
       print("CHILD, BEFORE PARENT altered()")
       super(Child, self).altered() #super相当于传递参数 运行parent,然后继续运行child
       print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
#output
"""
PARENT altered()
sss
CHILD, BEFORE PARENT altered()
PARENT altered()
sss
CHILD, AFTER PARENT altered()
"""