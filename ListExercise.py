fruit = ['mango', 'apple', 'cherry']
print("The data type is: ", type(fruit))
print(fruit)

fruit[2] = 'coconut'
print(fruit)

del fruit[1]
print(fruit)

print("length of list is", len(fruit))

fruit.insert(2, 'pear')
print(fruit)




fruit.append('peach')
print(fruit)

fruit.sort()
print("Sorted list : ", fruit)

fruit.reverse()
print("Reversed list : ", fruit)