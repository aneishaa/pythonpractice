#Write a Python program
# to find the sequences of one upper case letter followed by lower case letters?
import re
rule = '[A-Z]+[a-z]+$'
text = "Aw3erd"
matcher = re.fullmatch(rule,text)
if matcher != None:

  print("valid")
else:
    print("invalid")
