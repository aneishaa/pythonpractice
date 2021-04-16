import re
matcher = re.finditer('ab','absdabfgab')
count = 0
for match in matcher :
    count = count + 1
    print("match find at",match.start())
    print("match group",match.group())
print("count",count)