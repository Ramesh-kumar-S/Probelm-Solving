"""
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""

Arr = [-4,-1,0,3,10]
Res=[pow(X,2) for X in sorted(Arr)]
print(list(sorted(Res)))