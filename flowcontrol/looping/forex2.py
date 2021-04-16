lower = int(input("enter the lower"))
upper = int(input("enter the upper"))
upper = upper +1
evensum = 0
oddsum = 0
for i in range(lower,upper):
    if i % 2 ==0 :
     evensum = evensum + i
    else :
        oddsum = oddsum + i
print("odd number sum ",oddsum)
print("even sum ",evensum)