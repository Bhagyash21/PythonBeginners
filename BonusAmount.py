salary = float(input("Enter your salary : "))
yearofService = float(input("Enter years of service : "))
if yearofService >= 5:
    netBonusAmount = ((salary*5)/100) + salary
    print("Net Bonus Amount = ", netBonusAmount)
else:
    print("You are not eligible for bonus !")
