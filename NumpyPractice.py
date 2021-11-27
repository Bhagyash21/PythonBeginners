import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr[0])
print(arr[1:4])

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6,7])
arr3 = np.concatenate((arr1,arr2))
print(arr3)

newarr = np.array_split(arr3,3)
print(newarr)

arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr)

print("\n Basic operations search:")
arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr == 4)
print(x)

print("\n Sorting :")
arr = np.array([3,2,0,1])
print(np.sort(arr))


print("\n Trignometric functions are below: ")
import numpy as np

# create an array of angles
angles = np.array([0, 30, 45, 60, 90, 180])

# conversion of degree into radians
# using deg2rad function
radians = np.deg2rad(angles)

# sine of angles
print('Sine of angles in the array:')
sine_value = np.sin(radians)
print(np.sin(radians))

# inverse sine of sine values
print('Inverse Sine of sine values:')
print(np.rad2deg(np.arcsin(sine_value)))

# hyperbolic sine of angles
print('Sine hyperbolic of angles in the array:')
sineh_value = np.sinh(radians)
print(np.sinh(radians))

# inverse sine hyperbolic
print('Inverse Sine hyperbolic:')
print(np.sin(sineh_value))

# hypot function demonstration
base = 4
height = 3
print('hypotenuse of right triangle is:')
print(np.hypot(base, height))


#Slides Practice
print("\n Program1 from Slide")
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)

# Python program to demonstrate # Structured array
print("\n Program 2 from Slide:")
import numpy as np

a = np.array([('Sana', 2, 21.0), ('Mansi', 7, 29.0)],
             dtype=[('name', (np.str_, 10)), ('age', np.int32), ('weight', np.float64)])

# Sorting according to the name
b = np.sort(a, order='name')
print('Sorting according to the name', b)

# Sorting according to the age
b = np.sort(a, order='age')
print('\nSorting according to the age', b)


print("\n 3D array :")
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],
                [[7,8,9],[10,11,12]]])
for x in arr:
    print(x)

import numpy as np
from skimage import data
astranaut=data.astronaut()
print(astranaut)
print(astranaut.size)
