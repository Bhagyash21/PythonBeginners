#Write a program that reads an integer value from the user and prints output whether it is odd or even.

number = int(input("Enter a number : "))
if number % 2 == 0:
    print(number, 'is "even" ')
else:
    print(number, 'is "odd" ')

