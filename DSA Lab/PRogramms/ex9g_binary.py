# Iterative Binary Search Function method Python Implementation
# It returns the index of `n` in the given `list1` if present,
# else returns -1

def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        # Calculate the middle index (for an integer result)
        mid = (high + low) // 2

        # Check if `n` is present at `mid`
        if list1[mid] < n:
            low = mid + 1  # If `n` is greater, compare to the right of `mid`
        elif list1[mid] > n:
            high = mid - 1  # If `n` is smaller, compare to the left of `mid`
        else:
            return mid

    # Element was not present in the list, return -1
    return -1

# Initial `list1`
list1 = [12, 24, 32, 39, 45, 50, 54]
n = 45

# Function call
result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in `list1`")
