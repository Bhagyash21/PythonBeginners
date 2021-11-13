firstAmount = int(input("Enter the first amount in Celsius:"))
lastAmount = int(input("Enter the last amount in Celsius:"))
print("CELSIUS \t FAHRENHEIT")

for celsius in range(firstAmount, lastAmount+1):
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "         ", fahrenheit)
