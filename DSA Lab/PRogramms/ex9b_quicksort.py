# Python3 implementation of QuickSort

# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as the pivot
    pivot = array[high]
    # Pointer for the greater element
    i = low - 1

    # Traverse through all elements, comparing each element with the pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If an element smaller than the pivot is found,
            # swap it with the greater element pointed by i
            i = i + 1
            array[i], array[j] = array[j], array[i]

    # Swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # Return the position from where partition is done
    return i + 1

# Function to perform QuickSort
def quick_sort(array, low, high):
    if low < high:
        # Find the pivot element such that
        # elements smaller than the pivot are on the left
        # elements greater than the pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of the pivot
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of the pivot
        quick_sort(array, pi + 1, high)

# Driver code
array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)
print(f'Sorted array: {array}')
