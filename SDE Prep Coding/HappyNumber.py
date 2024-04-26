n=19

def happy(n):
    lookUpArr = []
    while n != 1:
        if n in lookUpArr:
            return False
        else:
            n = sum([pow(int(x),2) for x in str(n)])
            lookUpArr.append(n) 
    else:
        return True
    return False 
    #Recursive Approach
#     if n==1:
#         return "Happy"
#     else:
#         
#     Res=n
#     while Res>1:
#         Res=sum([pow(int(x),2) for x in str(Res)])
#         if Res == 1:
#              print("Yes")
#              break

print(happy(19))
    
