class Student :
    def __init__(self,rollno,name,course,total):
        self.rollno = rollno
        self.name = name
        self.course =course
        self.total = total
    # def __str__(self):
    #     print(self.name)
s1 = Student(1001,"priya","sse",600)
s2 = Student(1002,"wer","aaa",678)
s3 = Student(1003,"dddfs","ff",978)
studentlst = []
studentlst.append(s1)
studentlst.append(s2)
studentlst.append(s3)
stdtot = list(map(lambda stud:stud.total,studentlst))
#print(stdtot)
#print(max(stdtot))
develop = list(filter())

for m in stdtot:
    print(m)


