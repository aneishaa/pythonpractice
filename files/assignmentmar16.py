f = open("D:\luminart\customer.txt","r")
dictpplcnt = {}
agecnt = {}
profsncnt = {}
for lines in f  :
    data = lines.rstrip("\n").split(",")

    if data[1] not in dictpplcnt :
         dictpplcnt[data[1]] = 1
    else :
        dictpplcnt[data[1]] += 1
    if data[3] not in agecnt :
        agecnt[data[3]] = 1
    else :
        agecnt[data[3]]+= 1
    if data[-2] not in profsncnt :
        profsncnt[data[-2]] = 1
    else:
        profsncnt[data[-2]] += 1

print("working people count",dictpplcnt)
print("simillar age count",agecnt)
print("total profession count",profsncnt)
