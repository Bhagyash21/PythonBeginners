print("Calculator Application:")
option = int(input("Enter 1 for Addition: \n"
      "Enter 2 for Subtraction: \n"
      "Enter 3 for Multiplication: \n"
      "Enter 4 for Division: \n"
      "Enter 5 for Modulus : \n"))

def add(num1,num2):
      sum=num1+num2
      return sum

def subtract(num1,num2):
      diff = num1 - num2
      return diff

def multi(num1,num2):
      product = num1 * num2
      return product

def division(num1,num2):
      div = num1 / num2
      return div

def mod(num1,num2):
      modulus = num1 % num2
      return modulus

if option == 1:
      num1 = int(input("Enter number1 : "))
      num2 = int(input("Enter number2 : "))
      result = add(num1,num2)
      print(result)

elif option == 2:
      num1 = int(input("Enter number1 : "))
      num2 = int(input("Enter number2 : "))
      result = subtract(num1,num2)
      print(result)

elif option == 3:
      num1 = int(input("Enter number1 : "))
      num2 = int(input("Enter number2 : "))
      result = multi(num1,num2)
      print(result)

elif option == 4:
      num1 = int(input("Enter number1 : "))
      num2 = int(input("Enter number2 : "))
      result = division(num1,num2)
      print(result)

elif option == 5:
      num1 = int(input("Enter number1 : "))
      num2 = int(input("Enter number2 : "))
      result = mod(num1,num2)
      print(result)
else:
      print("Enter valid option")