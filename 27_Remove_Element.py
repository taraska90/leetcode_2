class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        # Input: nums = [0,1,2,2,3,0,4,2], val = 2
        # Output: 2, nums = [0,1,4,0,3]
        # [0,1,2,2,0,4,2]
        val_count = 0
        while 3 in nums:
            val_count += 1
            nums.remove(3)
        element_number = len(nums)
        return element_number

    def test(self):
        pass


a = Solution()
n, v = a.removeElement([3,2,2,3], 3)