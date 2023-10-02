nums = [1,2,3,4]

for i in nums:
    for inner_i in range(nums.index(i)):
        new_sum = nums.index(i) + nums[inner_i]
        print(new_sum)


