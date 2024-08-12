from memory_profiler import  profile

def power(num : int, pwr : int) -> int:
    if pwr == 0:
        return 1
    return num*power(num, pwr-1)
    
    
# print(power(2,11))

@profile
def factorial(num : int) -> int:
    if num == 0:
        return 1
    return num * factorial(num-1)

print(factorial(5))

#Iterative Approach
def fibonacci(n : int) -> int:
    fib=[0,1]
    Count=2
    while Count <= n:
        fib.append(fib[-2] + fib[-1])
        Count +=1
    return fib

from functools import  lru_cache

#Recursive Approach
@lru_cache(maxsize=None)
def fibonacci(n : int) -> int:
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))

@profile
def Prof():
    x=2
    y=26
    z=[x * 1000000000000000000 + y^26666666666666666666]
    s=z * 100000000
#     del z

Prof()