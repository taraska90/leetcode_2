class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        # Input: nums = [3, 2, 2, 3], val = 3
        # Output: 2, nums = [2, 2, _, _]
        val_count = 0
        while 3 in nums:
            val_count += 1
            nums.remove(3)
            nums.append('_')
