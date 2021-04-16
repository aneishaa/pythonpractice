line = "hello hai hello hai hello"
words = line.split(" ")
print(words)
dic1 = {}
for i in words :
    if i not in dic1 :
        dic1[i] = 1
    elif i in dic1 :
        dic1[i] += 1
for i in dic1 :
    print(i," :",dic1[i])
