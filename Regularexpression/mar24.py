import re
valid = []
rule = "[KK][il]\d{2}[a-zA-z]{2}\d{4}$"
f = open("vechicleno","r")
for num in f:
    number = num.rstrip("\n")
    matcher = re.fullmatch(rule,number)
    if matcher != None:
        valid.append(number)
print(valid)
