# import re
# x = "a+"
# r = "aaa abs aaa fff asd"
# matcher = re.finditer(x,r)
# for match in matcher:
#
#     print("match find at",match.start())
#     print("match group",match.group())

#
#
# import re
# x = "a?"
# r = "aaa dfr aaa fff asd"
# matcher = re.finditer(x,r)
# for match in matcher:
#
#     print("match find at",match.start())
#     print("match group",match.group())

# import re
# x = "a{2}"
# r = "aaa dfr aaa fff asd"
# matcher = re.finditer(x,r)
# for match in matcher:
#
#     print("match find at",match.start())
#     print("match group",match.group())

# import re
# x = "a{2,3}"
# r = "aaa dfr aaa fff asd"
# matcher = re.finditer(x,r)
# for match in matcher:
#
#     print("match find at",match.start())
#     print("match group",match.group())

# import re
# x = "^a"
# r = "aaa dfr aaa fff asd"
# matcher = re.finditer(x,r)
# for match in matcher:
#
#     print("match find at",match.start())
#     print("match group",match.group())
import re
x = "a$"
r = "aaa dfr aaa fff asa"
matcher = re.finditer(x,r)
for match in matcher:

    print("match find at",match.start())
    print("match group",match.group())


