class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

# Create a singly linked list
my_list = SLinkedList()
my_list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link the first Node to the second Node
my_list.headval.nextval = e2

# Link the second Node to the third Node
e2.nextval = e3

# Print the elements of the linked list
my_list.listprint()
