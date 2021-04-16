# python doesnot support overloading
class Person:
    def show(self,num1):
        self.num1 = num1
        self.num2 = num2
        print(self.num1,self.num2)
class Student(Person):
    def show (self,num1,num2):
        self.num1 = num1
        self.num2 =num2
        print(self.num1)
o1 =Student()
o1.show(2)