lst = []
nwlst = []

element = int(input("enter the length of list"))

for i in range (1,element+1):
    ele = int(input())
    lst.append(ele)
print(lst)
s = sum(lst)
print("sum=",s)
for i in lst:
    nwlst.append(s-i)
print(nwlst)







