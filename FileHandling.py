file = open("BhagyashreeFile.txt", 'r')
for each in file:
    print(each)

file2 = open("C:/Users/Admin/Desktop/AnotherFile.txt", 'r')
for each in file2:
    print(each)

# Python code to illustrate read() mode
file3 = open("BhagyashreeFile.txt", "r")
print("file3 Output:", file3.read())

# Python code to illustrate read() mode character wise
file4 = open("BhagyashreeFile.txt", "r")
print("file4 Output :", file4.read(5))



# Python code to create a file
file5 = open('satish.txt', 'w')
file5.write("This is the write command.")
file5.write("It allows us to write in a particular file.")
file5.close()

file5 = open('satish.txt', 'a')
file5.write("\n Appending this line to the file.")
file5.close()

file5 = open('satish.xls', 'w')
file5.write("This is the write command.")
file5.write("It allows us to write in a particular file.")
file5.close()

file5 = open('satish.doc', 'w')
file5.write("This is the write command.")
file5.write("It allows us to write in a particular file.")
file5.close()

file5 = open('satish.pdf', 'w')
file5.write("This is the write command.")
file5.write("It allows us to write in a particular file.")
file5.close()

file5 = open('satish.png', 'w')
file5.write("This is the write command.")
file5.write("It allows us to write in a particular file.")
file5.close()

file5 = open('satish.jpg', 'w')
file5.write("This is the write command.")
file5.write("It allows us to write in a particular file.")
file5.close()

#Python code to create a file in some other path:
file6 = open("C:/Users/Admin/Desktop/CreateAnotherFile.txt", 'w')
file6.write("This is the write command.")
file6.write("It allows us to write in a particular file")
file6.close()

#split() funstion
with open('satish.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
