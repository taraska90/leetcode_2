class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headvalue = None

    def printlist(self):
        newval = self.headvalue
        while newval:
            print(newval.value)
            newval = newval.next


    def find_last_node(self):
        newval = self.headvalue
        while newval:
            if newval.next:
                newval = newval.next
            else:
                last_node = newval
                return last_node

    def insert_beginning(self, begin_value):
        new_node = Node(begin_value)
        new_node.next = self.headvalue
        self.headvalue =  new_node

    def insert_end(self, end_value, linked_list):
        new_end_node = Node(end_value)
        last_node = linked_list.find_last_node()
        last_node.next = new_end_node

"""
list1 = SLinkedList()
list1.headvalue = Node(10)
e2 = Node(20)
e3 = Node(30)
list1.headvalue.next = e2
e2.next = e3
list1.insert_beginning(5)
list1.printlist()
"""