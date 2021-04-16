number = int(input("enter the number"))
if number > 1:
    # check for factors
    for i in range(2, number):
        print("+++++++",i)
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(number, "is not prime number")