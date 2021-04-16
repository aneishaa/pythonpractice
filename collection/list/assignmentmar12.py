lst1 = [1,2,3,4,5,6,7,8,9,10]
lst1.sort()
lst3= []
num  = int(input("enter the number"))

for i in lst1 :
    if i < num :
        lst3.append(i)
print(lst3)
first = lst3[0]
slicedlst = lst3[1:]
print(slicedlst)
for i in slicedlst:
    if i + first == num :

        print("(",i,",",first,")")

    else :
        first = i



