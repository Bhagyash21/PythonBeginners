age1 = int(input("Enter age of Person 1: "))
age2 = int(input("Enter age of Person 2: "))
age3 = int(input("Enter age of Person 3: "))
print("Age of Person 1:", age1)
print("Age of Person 2:", age2)
print("Age of Person 3:", age3)
if age1 >= age2 and age1 >= age3:
    print("Oldest is age1 :", age1)
elif age2 >= age1 and age2 >= age3:
    print("Oldest is age2 :", age2)
elif age3 >= age1 and age3 >= age2:
    print("Oldest is age3 :", age3)
else:
    print("All are equal")

