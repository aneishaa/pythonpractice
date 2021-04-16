lst = [10,20,30,40,50]
lst2 = [20,60,40,50,100]

lst3 = []
for i in lst :
    for j in  lst2:
        if i == j :
            lst3.append(i)
        else :
            pass
print(lst3)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []

[(result.append(i)) for i in a if i in b and i not in result]
print(result)