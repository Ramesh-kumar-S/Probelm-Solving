nums = [1,7,3,6,5,6]


left=0
for i in range(len(nums)):
    if left == sum(nums[i+1:]):
        print(i)
    left+=nums[i]
