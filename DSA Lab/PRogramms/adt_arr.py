# Python program to demonstrate
# Creation of Array

# Importing "array" for array creations
import array as arr

# Creating an array with integer type
a = arr.array('i', [1, 2, 3])

# Printing original array
print("The new created array is:", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# Creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# Printing original array
print("The new created array is:", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
