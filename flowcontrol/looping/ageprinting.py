birthdate  = int(input("enter the birthdate"))
birthmonth = int(input("enter the birthmonth"))
birthyear  = int(input("enter the  birth year"))
currentdate = int(input("enter the current date"))
currentmonth = int(input("enter the current month"))
currentyear = int(input("enter the  current year"))
if(currentmonth<birthmonth):
      currentyear = currentyear - 1
      age = currentyear - birthyear
      print("age =", age)
elif(currentmonth == birthmonth):
 if birthdate<=currentdate:
        age =  currentyear - birthyear
        print("age =", age)
 elif(birthdate>currentdate):
        currentyear = currentyear - 1
        age = currentyear - birthyear
        print("age =", age)
elif(currentmonth>birthmonth):
     age = currentyear - birthyear
     print("age =", age)

