lower = int(input("enter the lower"))
upper = int(input("enter the upper"))



for i in range(lower, upper+1):
       flag = 0
       for j in range(2,i):
          if(i%j == 0) :
            flag = 1
            break
          else:
            flag = 0
       if(flag == 0):
           print(i)

# if input number is less than
# or equal to 1, it is not prime

# if input number is less than
# or equal to 1, it is not prime
