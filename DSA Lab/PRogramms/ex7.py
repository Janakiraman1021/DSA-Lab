# Corrected code
list1 = [1, 2, 3, 4]

# Print the second element of the list (index 1)
print(list1[1])

# Print a slice from index 1 to 4 (exclusive), so elements at indices 1, 2, and 3
print(list1[1:4])

# Print the last element of the list
print(list1[-1])

# Initialize an empty list (list1 is now an empty list)
list1 = []

# Loop through indices from 0 to 10 (inclusive) and try to print corresponding elements (none are in the empty list, so this will raise an error)
for i in range(11):
    print(list1[i])

# Reassign list1 with values
list1 = [1, 2, 3, 4]

# Change the value at index 2 to 5
list1[2] = 5

# Print the modified list
print(list1)

# Extend the list with another list [1, 2, 3]
list1.extend([1, 2, 3])

# Print the extended list
print(list1)

# Initialize list1 with values
list1 = [1, 2, 3, 4, 5]

# Print the list
print(list1)

# Corrected code to delete an element at index 2 (not "Del" but "del" with a lowercase "d")
del list1[2]

# Print the modified list
print(list1)
