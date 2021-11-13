#Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.

intvalue = int(input("Enter the integer value : "))

if(intvalue == 1):
    print("Month {} is January".format(intvalue))
elif (intvalue == 2):
    print("Month {} is February".format(intvalue))
elif (intvalue == 3):
    print("Month {} is March".format(intvalue))
elif (intvalue == 4):
    print("Month {} is April".format(intvalue))
elif (intvalue == 5):
    print("Month {} is May".format(intvalue))
elif (intvalue == 6):
    print("Month {} is June".format(intvalue))
elif (intvalue == 7):
    print("Month {} is July".format(intvalue))
elif (intvalue == 8):
    print("Month {} is August".format(intvalue))
elif (intvalue == 9):
    print("Month {} is September".format(intvalue))
elif (intvalue == 10):
    print("Month {} is October".format(intvalue))
elif (intvalue == 11):
    print("Month {} is November".format(intvalue))
elif (intvalue == 12):
    print("Month {} is December".format(intvalue))
else :
    print("Please enter the number between 1 and 12. This number is invalid.")