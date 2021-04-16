class Employee:
    companyname = "IBM"

    def __init__(self,empid,empname,empsal):
        self.empid = empid
        self.empname = empname
        self.empsal = empsal

    def printDetail(self):
        print("empid", self.empid)
        print("Company", Employee.companyname)
        print("empname", self.empname)
        print("sal", self.empsal)


empid = int(input("enter the empid"))
empname = input("enter the empname")
empsal = int(input("enter the sal"))
o1 = Employee(empid,empname,empsal)

o1.printDetail()