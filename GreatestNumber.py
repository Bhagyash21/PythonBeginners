number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
if number1 > number2:
    print("{} is greater than {} !".format(number1,number2))
elif number2 > number1:
    print("{} is greater than {} !".format(number2,number1))
else:
    print("Both the numbers are equal!")
