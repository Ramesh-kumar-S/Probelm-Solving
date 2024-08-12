from collections import Counter
nums = [1,0,1,1]
# k = 3
# IndexMapping = {}
# for i,j in enumerate(nums):
#     IndexMapping[i] = j

FreqCounter = Counter(nums)
for K,V in FreqCounter.items():
    if V > 1:
        pass
        #add a for loop
        
nums = [1,2,3,4]
for n in range(len(nums)):
    prefix = nums[:n+1]
    suffix = nums[n:]
    print(prefix, suffix)



