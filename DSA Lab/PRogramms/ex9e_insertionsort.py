# Python program for the implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    # If the array has 1 or 0 elements, it's already sorted
    if (n := len(arr)) <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        # Move elements of arr[0..i-1] that are
        # greater than the key to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
