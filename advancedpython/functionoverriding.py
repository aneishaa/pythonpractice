# in function overriding child class  method overrides the parent class method
class Parent:
    def marry(self):
        print ("with arun")
class Child :
    def marry(self):
        print("with hima")
o1 = Child()
o1.marry()