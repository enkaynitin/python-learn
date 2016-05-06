# ex44a.py

class Parent(object):

    def implicit(self):
        print "PARENT implicit()"
        
class Child(Parent):
    pass
    
dad = Parent()
son = Child()
    
dad.implicit()
son.implicit()

# Output

PARENT implicit()
PARENT implicit()

# ex44b.py

class Parent(object):

    def override(self):
        print "PARENT override()"
        
class Child(Parent):

    def override(self):
        print "CHILD override()"
        
dad = Parent()
son = Child()

dad.override()
son.override()

# output

PARENT override()
CHILD override()

ex44c.py
class Parent(object):

    def altered(self):
        print "PARENT altered()"
        
class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altred()"
        super(Child,self).altered()
        print "CHILD, AFTER PARENT altered()"
        
dad = Parent()
son = Child()

dad.altered()
son.altered()

Output
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()


# ex44d.py

class Parent(object):

    def override(self):
        print "PARENT override()"
        
    def implicit(self):
            print "PARENT implicit()"
            
    def altered(self):
        print "Parent altered()"
        
class Child(Parent):

    def override(self):
        print "CHILD override()"
    
    def altered(self):
        print "CHILD BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
        
        
# output

PARENT implicit()
PARENT implicit()
PARENT override()
CHILD override()
Parent altered()
CHILD BEFORE PARENT altered()
Parent altered()
CHILD, AFTER PARENT altered()



# ex44e

class Other(object):
    
    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER altered()"
        
    def altered(self):
        print "OTHER altered()"
        
class Child(object):

    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print "CHILD override()"
    
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, BEFORE OTHER altered()"
    
son = Child()

son.implicit()
son.override()
son.altered()
        
# output

OTHER altered()
CHILD override()
CHILD, BEFORE OTHER altered()
OTHER altered()
CHILD, BEFORE OTHER altered()


