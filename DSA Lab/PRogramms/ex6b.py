# Function to calculate the sum of numbers from 1 to n
def sum(n):
    total = 0
    for index in range(n + 1):
        total += index
    return total

result = sum(5)
print(result)
