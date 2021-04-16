def add(num1,num2):
    sum = num1 + num2
    return sum
def mult(num1,num2):
    mult = num1 *num2
    return mult
def sub(num1,num2):
    sub = num1 - num2
    return sub
num1 = int(input("enter number"))
num2 = int(input("enter other number"))
add = add(num1,num2)
print("result is ", add)
mul = mult(num1,num2)
print("result of multiplication", mul)
subs = sub(num1,num2)
print("result substraction", subs)