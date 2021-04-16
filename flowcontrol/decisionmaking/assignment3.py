age = int(input("enter the age"))
sex = input("enter the sex M for Male F for female")
if sex == "F" :
    print("she can work only in urban area")
elif (sex == "M") & (20<age<=40) :

    print("can work anywhere")
elif (sex == "M") & (40 < age < 60):
    print("he can work only in urban area")
else :
    print("error in input")

