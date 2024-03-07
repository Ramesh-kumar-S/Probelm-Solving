Initialised = False
P=""
Result=[]
def superDigit(N,K):
    if len(N) == 1:
        return N
    else:
        global Initialised
        if not Initialised:
            P=N*K
            Initialised=True
            Res = [int(x) for x in P]
            superDigit(str(sum(Res)),K)
        else:
            Res = [int(x) for x in N]
            # print(Res)
            Result.append(sum(Res))
            superDigit(str(sum(Res)),K)
    
superDigit("148",3)
print(min(Result))
### Getting the Length of a List via Recursion

# A=[1,2,3,4,5]
# def getLenList(my_list):
#     if my_list == []:
#         return 0
#     return 1 + getLenList(my_list[1:])

# print(getLenList(A))
