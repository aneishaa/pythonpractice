from functools import reduce
lst = [10,20,30,40]
lst2 = reduce(lambda n1,n2:n1 + n2,lst)
print(lst2)
lst3 = reduce(lambda n1,n2 :n2 if n1>n2 else n2,lst)
print(lst3)