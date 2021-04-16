lst = [1,2,3,4]
nlst = [6,7,8,9]
squares = [num**2 for num in lst]
print(squares)
# lst2 = [(num1,mum2)]
evenlst = [num for num in lst if num%2 == 0]
print(evenlst)
pairs = [(i,j)for i in lst for j in nlst]
print(pairs)