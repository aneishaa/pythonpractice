def add (num1,num2) :
    sum= num1 + num2
    print("sum is", sum)
def sub (num1,num2):
    sub = num1 - num2
    print("sub is", sub)
def mult(num1,num2):
    mul = num1*num2
    print("mul is", mul)
def div (num1,num2):
    div = num1/num2
    print("div is", div)
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
choice = int(input("enter your choice 1 for add, 2 for sub,3for mul,4 divison"))
if choice == 1:
    add(num1,num2)
elif choice == 2:
    sub(num1,num2)
elif choice == 3:
    mult(num1,num2)
elif choice == 4:
    div(num1,num2)