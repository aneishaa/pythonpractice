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
      month = (12-birthmonth)+currentmonth
      print("month=", month)
elif(currentmonth == birthmonth):
 if birthdate<=currentdate:
        age =  currentyear - birthyear
        print("age =", age)
        print("month =", 0)
 elif(birthdate>currentdate):
        currentyear = currentyear - 1
        age = currentyear - birthyear
        print("age =", age)
elif(currentmonth>birthmonth):
     age = currentyear - birthyear
     print("age =", age)
     month = currentmonth - birthmonth
     print("month =", month)
if currentdate< birthdate :
    day =  birthdate - currentdate
elif currentdate> birthdate :
    day =  currentdate - birthdate
elif currentdate == birthdate:
    day = 0
print("days ",day)



