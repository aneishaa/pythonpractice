class oper:
    def add(self, n1, n2):
        res = n1 + n2
        print("res = ", res)


o1 = oper()
n1 = int(input("enter first number"))
n2 = int(input("enter second number"))
o1.add(n1, n2)