class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_nodes(self):
        new = self.value
        while new:
            print(new)
            new = new.next


#traversing node value
while new:
    print(new.value)
    new = new.next