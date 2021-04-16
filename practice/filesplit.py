filename = input("Input the Filename: ")
f_extn = filename.split(".")
print(f_extn)
print ("The extension of the file is : " + repr(f_extn[-1]))