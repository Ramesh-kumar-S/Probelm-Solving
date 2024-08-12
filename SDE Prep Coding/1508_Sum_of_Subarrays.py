nums = [1,2,3,4] 
n = 4
left = 1 
right = 5
sums = []
# for i in range(len(nums)):
#     for j in range(1,len(nums)-i+1):
#         sums.append(sum(nums[i:i+j]))
# print(sorted(sums))
# sums.sort()
# Res=0
# for i in range(left-1,right):
#     Res+=sums[i]
#     # print(sums[i])
# print(Res)



for i in range(len(nums)):
    for j in range(i, len(nums)):
        print(nums[i:j+1])