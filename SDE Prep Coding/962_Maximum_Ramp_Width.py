nums = [9,8,1,0,1,9,4,0,4,1]
# nums = [6,0,8,2,1,5]
# Res=[]
nums=[0,1]
max_value=0
for i in range(len(nums)-1):
    for j in range(i,len(nums)):
        if i < j and nums[i] <= nums[j]:
            print(i,j, j-i)
            if j-i > max_value:
                max_value = j-i
        