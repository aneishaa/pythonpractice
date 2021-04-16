lst = [3,5,2,9,8,4,8]
lst.sort()
print(lst)
low = 0
f = "a"
upper = len(lst)-1
element = int(input("enter an element"))
l = len(lst)
while( low <= upper):

   mid = (low + upper)//2
   if element>lst[mid] :
       low = mid + 1
   elif element < lst[mid]:
       upper = mid - 1
   elif element ==lst[mid]:
        print("element found")
        f = "found"
        break


   l = l-1
if f != "found":
    print("not found")



