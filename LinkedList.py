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

    def insert_node(self, value):
        new_node = Node(value)
        root = self.headvalue
        while root:
            root.next = new_node


    def insert_beginning(self, begin_value):
        new_node = Node(begin_value)
        new_node.next = self.headvalue
        self.headvalue = new_node

    def insert_end(self, end_value, linked_list):
        new_end_node = Node(end_value)
        last_node = linked_list.find_last_node()
        last_node.next = new_end_node


    def insert_middle(self, middle_val, new_val):
        if middle_val is None:
            print("mentioned node is absent")
            return
        new_node = Node(new_val)
        new_node.next = middle_val.next
        middle_val.next = new_node

    def remove_node(self, key_to_remove):
        head_val = self.headvalue
        while head_val is not None:
            if head_val.next.value == key_to_remove:
                head_val.next = head_val.next.next
            else:
                head_val = head_val.next


"""
list1 = SLinkedList()
list1.headvalue = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headvalue.next = e2
e2.next = e3
list1.insert_beginning(5)
list1.printlist()
list1.insert_node("Tue")
"""