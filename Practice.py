for i in range(0, 6):
    for j in range(i):
        print(i, end=' ')
    print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(0, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print("\n")
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

print("\n")
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print("5", end=' ')
    print()
# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5


print("\n")
for i in range(5, 0, -1):
    for j in range(0, i):
        print("5", end=' ')
    print()
# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5


print("\n")
for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=' ')
    print()
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

print("\n")
for i in range(0, 6):
    for j in range(0, i):
        print(i, end=' ')
        i = i - 1
    print()
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1


print("\n")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(i, end=' ')
        i = i-1
    print()
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


a = input("Enter the name:")
for i in a:
    if i == a[0]:
        print(a[0], end='')
    elif i == a[len(a)-1]:
        print(a[-1])
    else:
        print("*", end='')