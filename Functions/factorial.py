def fact():
    num = int(input("enter the number"))
    factorial = 1
    while(num>=1):
        factorial = factorial * num
        num = num - 1
    print(factorial)
fact()

