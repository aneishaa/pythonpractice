# x='[abc]' either a b or c
# x='[^abc]' except abc
# x='[a-z]' a to z
# x='[A-Z]' A to Z
# x='[a-zA-Z]' both lower and upper case are checked
# x='[0-9]' check digits
# x='[^a-zA-Z0-9]' special symbols
# x='\s' check space
# x='\d' check the digits
# x='\D' except digits
# x='\w' all words except special characters
# x='\W' for special characters
import re
#check for either a or b or c
# x = "[abc]"
# matcher = re.finditer(x,'absdabfgabc')
#
# for match in matcher :
#
#     print("match find at",match.start())
#     print("match group",match.group())
#except abc**************
# x = "[^abc]"
# matcher = re.finditer(x,'absdabfgabc')
#
# for match in matcher :
#
#     print("match find at",match.start())
#     print("match group",match.group())
#check for letters from a to z
# x = "[a-z]"
# matcher = re.finditer(x,'absdabfga##bc')
#
# for match in matcher :
#
#     print("match find at",match.start())
#     print("match group",match.group())


matcher = re.finditer(x,'absdabf  ga##bc')

for match in matcher :

    print("match find at",match.start())
    print("match group",match.group())

