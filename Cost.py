quantity = float(input("Enter the quantity: "))
totalCost = quantity*100
if totalCost >= 1000:
    costAfterDiscount = totalCost - ((totalCost*10)/100)
    print("The total cost of the purchase is: ", totalCost)
    print("Cost after discount to be paid by user is : ", costAfterDiscount)
else:
    print("No discount offered,as purchase amount is less than 1000. Total amount to be paid by User is :", totalCost)
