# Python program to
# demonstrate implementation of
# queue using the queue module
from queue import Queue

# Initializing a queue
q = Queue(maxsize=3)

# qsize() gives the maxsize
# of the Queue
print(q.qsize())

# Adding elements to the queue
q.put('a')
q.put('b')
q.put('c')

# Return Boolean for Full Queue
print("\nFull:", q.full())

# Removing elements from the queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty Queue
print("\nEmpty:", q.empty())

# Adding another element to the queue
q.put(1)
print("\nEmpty:", q.empty())
print("Full:", q.full())

# If you uncomment the line below, it will result in an Infinite Loop as the Queue is empty.
# print(q.get())
