
import re
valid = []
rule = "[L][U][M][0-9]{2}[P][Y][0-9]{3}$"
f = open("rollno","r")
f2 = open("result.txt", "a")
for num in f:
    number = num.rstrip("\n")
    matcher = re.fullmatch(rule,number)
    if matcher != None:
        valid.append(number)
        f2.write(number)
        f2.write("\n")


print(valid)