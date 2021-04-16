lst = []
evenlst= []
oddlst = []
for i in range(50,201):
    lst.append(i)
print(lst)
for i in lst:
    if i  % 2 == 0:

        evenlst.append(i)
    else:

        oddlst.append(i)
print("even list ")
print(evenlst)
print("odd list ",oddlst)
