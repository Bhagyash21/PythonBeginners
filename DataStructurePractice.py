'''Sets'''
aSet = set(('Apple', 'Banana','Orange'))
print(aSet)

'''Dictionaries'''
dict = {'H': 'Hydrogen',
                  'He': 'Helium',
                  'Li': 'Lithium',
                  'Be': 'Berilium',
                  'B': 'Boron',
                   1: 'DuplicateB'
        }
print(dict)
print("Items of dictionary are: \n", dict.items())

print(dict.keys())

print(dict.values())

dict.update({'P':'Phosphorous','S':'Sulphur'})
print(dict)

del dict[1]
print(dict)

print(dict['H'])
print(dict['B'])
#print(dict['h']) #It is case sensitive

