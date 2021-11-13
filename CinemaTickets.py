#CinemaTickets

age = float(input("Enter your age: "))
fullPrice = 6

if age < 16:
    print("Your ticket costs £", fullPrice/2)
elif age >= 60:
    print("Your ticket costs £", fullPrice/3)
else:
    print("Your ticket costs £", fullPrice)
