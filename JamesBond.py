print("Try and name 4 actors who have played James Bond.")
ctr = 0
for i in range(1, 5):
    actorName = input("Attempt {} - Name an actor: ".format(i)).lower()
    if actorName == 'roger moore':
        print(" Well done: Roger Moore was Bond in Live and Let Die.")
        ctr = ctr + 1
    elif actorName == 'sean connery':
        print("Well done: Sean Connery was Bond in From Russia with Love.")
        ctr = ctr + 1
    elif actorName == 'will smith':
        print(" Sorry. Will Smith hasn’t played Bond as far as I know.")
    elif actorName == 'daniel craig':
        print("Well done: Daniel Craig was Bond in Skyfall.")
        ctr = ctr + 1
    else:
        print("Incorrect actor name")
print("You got", ctr, "out of 4")