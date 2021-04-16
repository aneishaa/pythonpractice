lst = []

lst.extend([1,2,3,4,5])
print(lst)
flag = 0
element = int(input("enter an element"))
for i in lst:
    if i == element:
        print("element found")
        flag = 1
        break
    else:
        flag = 2

if flag == 2:
    print("element not found")

