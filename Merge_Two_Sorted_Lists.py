class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        [list1.append(i) for i in list2]
        list1.sort()
        return list1