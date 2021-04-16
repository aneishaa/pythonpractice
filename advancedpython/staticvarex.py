class Employee:
       companyname = "IBM"

       def readdetail(self, empid, empname, empsal) :
         self.empid = empid
         self.empname = empname
         self.empsal = empsal
        

       def printDetail(self):
            print("empid", self.empid)
            print("Company", Employee.companyname)
            print("empname", self.empname)
            print("sal", self.sal)
        

empid = int(input("enter the empid"))
empname = input("enter the empname")
empsal = int(input("enter the sal"))
o1 = Employee()
o1.readdetail(empid,empname,empsal)
o1.printDetail()