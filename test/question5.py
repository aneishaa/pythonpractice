#What is method overriding give an example using Books class?
class Book:
    def General(self):
        print ("General books")
class Child :
    def General(self):
        print("Thriller books")
o1 = Child()
o1.General()