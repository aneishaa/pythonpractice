import re
valid = []
rule = '[a-zA-z0-9]+@[a-zA-Z0-9]+\.[a-zA-z0-9]+$'

mail = "ani@gmail.com"


matcher = re.fullmatch(rule,mail)
if matcher != None:

  print("valid")
else:
    print("invalid")
