weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))
BMI = weight/(height*height)
print("Your BMI is:", round(BMI, 2))
if BMI <= 18.5:
    print('You are in the “Underweight” range.')
elif (BMI > 18.5 and BMI <= 24.9):
    print('You are in the “Normal” range.')
elif (BMI >= 25 and BMI <= 29.9):
    print('You are in the “Overweight” range.')
else:
    print('You are in the “Obese” range.')



