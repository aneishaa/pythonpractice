#combination of uppercase lowercase ending with a number
# import re
# valid = "AABGq3"
# rule = '[a-zA-z]+\d{1}$'
#
# matcher = re.fullmatch(rule,valid)
# if matcher != None:
#
#   print("valid")
# else:
#     print("invalid")

# import re
# valid = "ab"
# rule = "(^a[a-zA-z0-9\w]*b$)"
#
# matcher = re.fullmatch(rule,valid)
# if matcher != None:
#
#   print("valid")
# else:
#     print("invalid")
#************888888888program to check certain set of characters
# import re
# valid = "ABCDEFabcdef123450"
# rule = (r'[^a-zA-Z0-9.]')
# matcher = re.fullmatch(rule,valid)
# if matcher != None:
#
#     print("valid")
# else:
#      print("invalid")
#Python program that matches a string that has an a followed by zero or more b's
# import re
# def text_match(text):
#         patterns = 'ab*?'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("qc"))
# print(text_match("abc"))
# print(text_match("abbc"))
#a Python program that matches a string that has an a followed by one or more b's.
# import re
# def text_match(text):
#         patterns = 'ab+?'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("abe"))
# print(text_match("abc"))
# a Python program that matches a string that has an a followed by zero or one 'b
# import re
# def text_match(text):
#         patterns = 'ab?'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("ag"))
# print(text_match("abc"))
# print(text_match("abbc"))
# print(text_match("aabbc"))
# # Python program that matches a string that has an a followed by three 'b'.

# import re
# def text_match(text):
#         patterns = 'ab{3}'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("abbc"))
#a Python program that matches a string that has an a followed by two to three 'b

# import re
# def text_match(text):
#         patterns = 'ab{2,3}'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("ab"))
# Python program to find sequences of lowercase letters joined with a underscore.
# import re
# def text_match(text):
#         patterns = '^[a-z]+_[a-z]+$'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("ab_cA"))
# Python program to find the sequences of one upper case letter followed by lower case letters.
# import re
# def text_match(text):
#         patterns = '^[A-Z]+[a-z]+$'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("ABCabxc"))
#a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# import re
# def text_match(text):
#         patterns = '[a]*?[b]$'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("agfdshh####b"))
# a Python program that matches a word at the beginning of a string.
import re
# def text_match(text):
#         patterns = '^\w+'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("HAI "))
#a Python program that matches a word at the end of string, with optional
# import re
# def text_match(text):
#         patterns = '\w+\S*$'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("####  HAI"))
#a Python program that matches a word containing 'z'
import re
# def text_match(text):
#         patterns = '\w*z./w*'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("worzdf"))
#Python program that matches a word at the end of string, with optional punctuation
# import re
# def text_match(text):
#         patterns = '\Bz\B'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
#
# print(text_match("hfdfjjz"))
#Python program that matches a word containing 'z'
#patterns = '\w*z.\w*'
# a Python program that matches a word containing 'z', not at the start or end of the word.
#'\Bz\B'
#to match a string that contains only upper and lowercase letters, numbers, and underscores
#Python program to match a string that contains only upper and lowercase
# letters, numbers, and underscores
#patterns = patterns = '^[a-zA-Z0-9_]*$'
#program where a string will start with a specific number
# text = re.compile(r"^5")
# to remove leading zero string = re.sub('\.[0]*', '.', ip)

import re
def text_match(text):
        #patterns = '[A-Z][a-z][0-9][-$'
        patterns = '[^0-9]{8,15}$'
        if re.search(patterns,  text):

                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("zhfzdhjgsfj4sdgfjs"))


