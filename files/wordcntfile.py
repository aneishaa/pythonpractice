# f = open("randmtxt","r")
# words = []
# dic = {}
# for lines in f  :
#    # print(lines)
#     words = lines.rstrip("\n").split()
# print(words)
# for i in words
#     if i not in dic:
#         dic[i] = 1
#     elif i in dic1 :
#         dic[i] += 1
# for i in dic:k
#     print(i," :",dic[i])
f= open("randmtxt","r")
dic = {}
for line in f:
    words = line.rstrip("/n").split()
print(words)
for i in words :
    if i not in dic :
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)
