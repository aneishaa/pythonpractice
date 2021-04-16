employee = [[1001,"john",15000],[1002,"hari",25000],[1003,"leo",20000]]
# for i in employee :
#     if i[2]>15000:
#         print(i[1])
#
totsal = 0
for i in employee :
    totsal =  totsal + i[2]
print(totsal)