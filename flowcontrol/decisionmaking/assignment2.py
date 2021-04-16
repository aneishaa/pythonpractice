totclasses = int((input("enter the total number of classes")))
attentedclasses = int((input("enter the total number of attented classes")))
attenpercent = (attentedclasses/totclasses) * 100
print("attendence percentage =",attenpercent)
if attenpercent < 75 :
    print("cannot attend exam")
else :
    print("can attend exam")