f = open("numbers","r")
evenlst = []
oddlst = []
for lines in f  :
    if int(lines) %2 == 0 :
        evenlst.append(int((lines.rstrip("\n"))))
    else :
        oddlst.append(int((lines.rstrip("\n"))))
   # if first strip then use  lstrip
evensum = sum(evenlst)
print("even sum",evensum)
oddsum = sum(oddlst)
print("odd sum",oddsum)