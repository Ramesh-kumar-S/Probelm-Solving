def sumofN(n : int):
    if n==1:
        return n
    else:
        print(n,n-1)
        return n+sumofN(n-1)

# print(sumofN(5))

def Run(n :int):
    if n==0:
        return n
    else:
        print(n)
        Run(n-1)
        Run(n-1)
        
Run(3)
print("Hello Ramesh")


