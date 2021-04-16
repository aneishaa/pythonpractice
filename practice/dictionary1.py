# d = {'x': 10, 'y': 20, 'z': 30}
# for dict_key, dict_value in d.items():
#     print(dict_key,'->',dict_value)
# n=int(input("Input a number "))
# d = dict()
#
# for x in range(1,n+1):
#     d[x]=x*x
#
# print(d)
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d = d1.copy()
#
# d.update(d2)
# print(d)
#
# d = {'Red': 1, 'Green': 2, 'Blue': 3}
# for color_key, value in d.items():
#      print(color_key, 'corresponds to ', d[color_key])

d = {'Red': 1, 'Green': 2, 'Blue': 3}
totcol = 0
print(sum(d.values()))