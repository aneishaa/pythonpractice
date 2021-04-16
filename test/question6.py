# Create objects of the following file and print the
# details of student with maximum mark
class Student :
    school= "GMM"
    def detail(self,name,age,cn,mark):
        self.name = name
        self.age = age
        self.cn = cn
        self.mark = mark

        print("school name",self.school)
        print("name ",self.name)
        print("age",self.age)

f = open("studentdetail","r")
datanew = []


for lines in f :
    data = lines.rstrip("\n").split(",")

    datanew.append(data)

temp = 0
marks= []
for i in datanew:
          marks.append(i[3])
          maxvalue =max(marks)
for i in datanew:
    obj = Student()
    if maxvalue == i[3]:
        obj.detail(i[0],i[1],i[2],i[3])