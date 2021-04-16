# Single inheritence
class Parent:
    parent_name = "Arun"
    def m1(self,age):
        self.age = age
        print("parent",Parent.parent_name)
        print("age",self.age)
class Child(Parent):
     def m2(self):
         print("parentname",Parent.parent_name)
         print("age",self.age)
c1 = Child()
c1.m1(23)
c1.m2()