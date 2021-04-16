# Create an example for three types of inheritance in one
# program by using Person as main class?
class Parent:
    parent_name = "Arun"
    def m1(self,age):
        self.age = age
        print("parent",Parent.parent_name)
        print("age",self.age)
class Child(Parent):
     def m2(self,name):
         self.name = name
         print("parentname",Parent.parent_name)
         print("age",self.age)

class Kid(Child):
    def m3(self):
        print("parentname", Parent.parent_name)
        print("age", self.age)
        print("name", self.name)
c1 = Kid()
c1.m1(23)
c1.m2("priya")
c1.m3()