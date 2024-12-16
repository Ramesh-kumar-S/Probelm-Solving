"""
Write a program that prints out every number from 1-100 that is divisible by 3 or 5 with no remainder.
"""
Output = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0]
print(" ".join(list(map(str, Output))))
