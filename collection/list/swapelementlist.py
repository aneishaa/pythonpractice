l = [1,2,3,4,5]
mid = l[0]
l[0] = l[-1]
l[-1] = mid
print(l[0])
print(l[-1])