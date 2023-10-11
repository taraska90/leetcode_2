from Merge_Two_Sorted_Lists import *

list1 = [1,2,4]
list2 = [1,3,4]
output = [1,1,2,3,4,4]

test = Solution()
result = test.mergeTwoLists(list1, list2)

if result == output:
    print("Test is PASSED")
else:
    print("Test is FAILED")