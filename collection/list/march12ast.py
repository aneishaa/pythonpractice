lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst1.sort()
lst3 = []
num = int(input("enter the number"))

for i in lst1:
    if i < num:
        lst3.append(i)
print(lst3)
lst4 = lst3

for i in lst3:
    for j in lst4 :
        if i + j == num :
            print("(",i,",",j,")")