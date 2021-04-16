#Create a valid phone numbers file from the following file?
# +915678905432 +914567890321 765432167 123450987765 +919976532456


import re
valid = []
rule = "[+][9][1]\d{10}"
f = open("phoneno","r")
for num in f:
    number = num.rstrip("\n")
    matcher = re.fullmatch(rule,number)
    if matcher != None:
        valid.append(number)
print(valid)
