class Person :
    def setVal(self,num,age):
        self.num = num
        self.age = age
    def printVal(self):
        print("num",self.num)
        
    def Walk(self):
        print("walking ")
obj1 = Person()
obj1.Walk()