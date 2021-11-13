amountinPounds = float(input("PLease enter amount in pounds :"))
amountinDollar = amountinPounds * 1.38
print("Pound",amountinPounds," are Dollar" ,amountinDollar)


#Another way using format

amountinPounds = float(input("PLease enter amount in pounds :"))
amountinDollar = amountinPounds * 1.38
print("£ {} are $ {}".format(amountinPounds,amountinDollar))
print("£ {0} are $ {1}".format(amountinPounds,amountinDollar))
