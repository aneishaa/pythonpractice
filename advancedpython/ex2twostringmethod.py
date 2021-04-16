class Employee :
    companyname = "ibs"
    def __init__(self,empid,empname):
        self.empid = empid
        self.empname = empname
    def printval(self):
        print("company",self.companyname)
        print("empid ",empid)
        print("name",self.empname)
    def __str__(self):
        return str(self.empid)
o1 = Employee(1001,"ani")
print(o1)