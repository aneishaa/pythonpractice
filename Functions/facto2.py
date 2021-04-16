def fact(num):

    factorial = 1
    while(num>=1):
        factorial = factorial * num
        num = num - 1
    print(factorial)
num = int(input("enter the number"))
fact(num)