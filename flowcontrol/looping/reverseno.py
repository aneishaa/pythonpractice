# program to reverse number
number = int(input("enter the number"))
result = 0
while(number!=0):
    reverse = number%10
    result = (result * 10) + reverse
    number = number // 10
print("reverse",result)