def div_deco(func):
    def inner(num1,num2):
        if num1<num2 :
            (num1,num2) = (num2,num1)
        return func(num1,num2)
    return inner
@div_deco
def div(num1,num2):
    return num1/num2
s = div(10,50)
print(s)
