num1 = int(input("enter the  first number"))
num2 = int(input("enter the second number"))
num3 = int(input("enter the third number"))
firstlargest = 0
if(num1==num2==num3):
  print("numbers are equal")


if (num1 > num2) & (num1 >num3):
    firstlargest = num1
elif(num2>num1) & (num2 > num3):
    firstlargest = num2
elif (num3 > num1) & (num3 > num2):
    firstlargest = num3
print("largest",firstlargest)

if firstlargest == num1 :
    if (num2 > num3) :

          print("second largest is " , num2)
    else :
        print("second largest is " , num3)
if firstlargest == num2 :
    if num1 > num3 :
        print("second largest is " , num1)
    else :
        print("second largest is " , num3)
if firstlargest == num3:
    if num1 > num2 :
        print("second largest is " , num1)
    else :
        print("second largest is " , num2)

