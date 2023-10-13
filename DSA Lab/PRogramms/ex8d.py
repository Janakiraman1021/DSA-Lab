class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

my_list = SLinkedList()
my_list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

my_list.headval.nextval = e2
e2.nextval = e3

my_list.Inbetween(my_list.headval.nextval, "Fri")
my_list.listprint()
