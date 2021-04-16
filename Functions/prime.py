def isprime():
  number = int(input("enter a number"))
  if number == 2:
      print("is prime")
  flag = 0
  for i in range(2, number):

    if (number % i) == 0:
        flag = 1
        break
    else:
        flag = 0
  if flag == 1:
      print("not prime")
  else:
      print("prime")
isprime()