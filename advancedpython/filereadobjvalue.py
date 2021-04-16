class Employee :
    companyname = "IBM"
    def detail(self,name,age,cn,mark):
        self.name = name
        self.age = age
        self.cn = cn
        self.mark = mark
        if int(self.mark) > 190:
            print("company name",self.companyname)
            print("name ",self.name)
            print("age",self.age)

f = open("readobjvalue","r")
datanew = []
# obj1 = ["o1","o2","o3","o4","o5"]

for lines in f :
    data = lines.rstrip("\n").split(",")

    datanew.append(data)
# print(datanew)
# print(datanew[0])

for i in datanew:
        obj = Employee()

        obj.detail(i[0],i[1],i[2],i[3])





