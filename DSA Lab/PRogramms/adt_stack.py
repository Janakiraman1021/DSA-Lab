# Simple ADT using Stack using List

# Python program to demonstrate stack implementation using a list
stack = []

# append() function to push elements onto the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)

# pop() function to pop elements from the stack in LIFO (Last-In, First-Out) order
print('\nElements popped from the stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# Uncommenting print(stack.pop()) will cause an IndexError as the stack is now empty.
