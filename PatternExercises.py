print("Pattern 1 : ")
for i in range(1,6):
    for j in range(0,i):
        print(i, end=' ')
    print()

print("\n Another way for Pattern 1 : ")
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

print("\n Pattern 2 : ")
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

print("\n Pattern 3 : ")
for i in range(5):
        for j in range(0,i+1):
            print(j,end=" ")
        print('')


print("\n Pattern 4 : ")
for i in range(1,6):
        for j in range(0,6-i):
            print(i,end=" ")
        print('')

print("\n Another way for Pattern 4 : ")
for i in range(1,6):
    for j in range(i,6):
        print(i,end=" ")
    print()

print("\n Another way for Pattern 4 : ")
for i in range(0,5):
    for j in range(0,5-i):
        print(i+1,end=" ")
    print()

print("\n Pattern 5 : ")
for i in range(0, 5):
    for j in range(0, 5-i):
        print("5", end=' ')
    print()

print("\n Pattern 6: ")
for i in range(1,6):
    for j in range(i,0,-1):
       print(j, end=" ")
    print()
#
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

print("\n Pattern 7: ")
n='Python'
x=len(n)
for i in range(0,x+1):
  print(n[:i])
print()

print("\n Another way for Pattern 7: ")
word = 'Python'
x = ''
for i in word:
    x = x + i
    print(x)

print("\n Another way for Pattern 7: ")
language = "Python"
for i in range(6):
    print("")
    for j in range(0, i+1):
        print(language[j], end="")


print("\n Pattern 8: ")
# A
# B C
# D E F
# G H I J
# K L M N O
# P Q R S T U
# V W X Y Z [ \

alphabets = 65
for i in range(0, 7):
    for j in range(0, i+1):
        print(chr(alphabets), end=' ')
        alphabets = alphabets + 1
    print()

