pattern  = "ABCDAGH"
dic = {}
for ch in pattern :
    if ch not in dic :
        dic[ch] = 1
    elif ch in dic :
        print("first recursive",ch)
        break


