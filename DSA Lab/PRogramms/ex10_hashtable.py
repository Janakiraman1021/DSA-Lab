# Python program to demonstrate working of HashTable
# Initialize the hash table as a list of 10 empty lists
hashTable = [[] for _ in range(10)]

# Function to check if a number is prime
def checkPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to get the next prime number greater than n
def getPrime(n):
    if n <= 1:
        return 2
    prime = n + 1
    while True:
        if checkPrime(prime):
            return prime
        prime += 1

# Function to compute the hash index using the modulo operator
def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

# Function to insert data into the hash table
def insertData(key, data):
    index = hashFunction(key)
    hashTable[index].append((key, data))

# Function to remove data from the hash table
def removeData(key):
    index = hashFunction(key)
    for item in hashTable[index]:
        if item[0] == key:
            hashTable[index].remove(item)

# Inserting data into the hash table
insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

# Printing the hash table
print(hashTable)

# Removing data from the hash table
removeData(123)

# Printing the hash table after removal
print(hashTable)
