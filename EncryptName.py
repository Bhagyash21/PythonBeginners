name = input("Please enter your name: ".capitalize())
print("Encrypted form is", name[0], "*" * (len(name)-2), name[-1])
print("Encrypted form is", name[0]+"*" * (len(name)-2)+name[-1])

#Way2:
print("\n Way 2 to encrypt:")
goodname = input("Please enter your name:").capitalize()
encryptedname = goodname.replace(goodname[1:len(goodname)-1],"*"*(len(goodname)-2))
print(encryptedname)

#Way3 using for loop:
#for i in range(name[1],len(name)):
print("\n Way 3 using for loop:")
fName = input("please enter first name :")
for i in range(len(fName)):
    if i == 0 or i == len(fName)-1:
        print(fName[i], end="")
    else:
        print("*", end="")



