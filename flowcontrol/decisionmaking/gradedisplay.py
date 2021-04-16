mark1 = int(input("enter the mark1 out of 50 "))
mark2 = int(input("enter the mark1 out og 50"))
mark3 = int(input("enter the mark1 out og 50"))
mark4= int(input("enter the mark1 out og 50"))

percn = ((mark1+mark2+mark3+mark4)/200)* 100
print("percn",percn)
if(percn>=90):
    print("grade A+")
elif (percn <90) & (percn >= 80):
    print("grade A")
elif (percn >=70) & (percn <80):
    print("grade B+ ")

elif (percn >=60) & (percn <70):
    print("grade B ")
elif (percn >=50 )& (percn < 60):
    print("grade c+ ")
elif (percn >=40) & (percn < 50):
    print("grade c ")
elif (percn >=30) & (percn < 40):
    print("grade d+ ")
elif (percn < 30):
    print("fail")