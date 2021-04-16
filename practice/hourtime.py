def convert(num):
    if num < 60 :
        hr = 0

        min = num
    if num == 60 :
        hr =1
        min = 0
    if num >60:
        min = num % 60
        hr = num // 60
    print(hr,":",min)
num = 100
convert(num)


