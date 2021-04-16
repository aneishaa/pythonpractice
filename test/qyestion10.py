# a Python program that matches a string that has an
# 'a' followed by anything, ending in 'b'?
import re
rule = 'a.*?b$'
text = "aw3erb"
matcher = re.fullmatch(rule,text)
if matcher != None:

  print("valid")
else:
    print("invalid")
