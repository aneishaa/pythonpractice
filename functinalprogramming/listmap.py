lst = [3,2,4,5,6,7,8,9]
result = list(map(lambda n:n+1 if n>5 else n-1,lst))
print(result)