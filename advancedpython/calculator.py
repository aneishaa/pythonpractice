class Calculator:


    def __init__(self,op1,op2):
        self.op1 = op1
        self.op2 = op2


    def add(self):
       res = self.op1 + self.op2
       print("res=",res)
    def div(self):
        res = self.op1 / self.op2
        print("res=", res)
    def sub(self):
       res = self.op1 - self.op2
       print("res=",res)
    def mul(self):
       res = self.op1 * self.op2
       print("res=",res)


op1 = int(input("enter the firstno"))
op2 = int(input("enter the secondno"))

o1 = Calculator(op1,op2)

o1.add()
o1.mul()
o1.div()