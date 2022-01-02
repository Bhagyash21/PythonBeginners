sentence = input("Enter a string: ")
splitsentence = sentence.split(" ")
revtext = list(reversed(splitsentence))
rev = " ".join(revtext)
for words in rev:
    if words.islower():
        print(words.upper(), end='')
    else:
        print(words.lower(), end='')






