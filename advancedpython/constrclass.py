class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printVal(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno = rollno
        self.mark = mark
    def print(self):
        print(self.rollno)
        print(self.mark)
ob1 = Student(1,537,"ani",35)
ob1.printVal()
ob1.print()

