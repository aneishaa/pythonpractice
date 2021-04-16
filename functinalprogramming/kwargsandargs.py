def valueprint(*args):
    print(args)
def valprint(**kwargs):
    print(kwargs)
    # for k,value in kwargs.items():
    #     print(k,"-->",value)
valueprint(10,20,30)
valprint(maths="10",science="9",english="10")
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
#
#
# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')
