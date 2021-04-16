f = open("numbers","r")
list2 = []
for lines in f  :
   # print(lines)
    list2.append(lines.rstrip("\n"))
   # if first strip then use  lstrip
sum = 0
for i in list2 :
    sum = sum + int(i)

print(sum)