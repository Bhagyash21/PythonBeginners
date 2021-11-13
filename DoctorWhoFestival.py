print("Doctor Who Festival - Price Calculator \n Note: enter 0 if none")
individuals = int(input("Enter total number of individuals : "))
under16 = int(input("Enter total number of under 16s: "))
families = int(input("Enter total number of families :"))

individualPrice = individuals * 68
under16Price = under16 * 32.25
familiesPrice = families * 42.75

print("Category Price Breakdown: \n Price is £{} for {} individuals \n Price is £{} for {} under 16s \n "
      "Price is £{} for {} families".format(individualPrice,individuals,under16Price,under16,familiesPrice,families))

persons = under16 + individuals + (families * 4)
eventPrice = individualPrice + under16Price + familiesPrice

print("Total Persons are {} \n "
      "Total Event Price is £{} \n "
      "More info and booking visit our website".format(persons,eventPrice))


