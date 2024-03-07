from operator import index, indexOf


String="hackerrank"
Input="rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"
Res=[]
L_Inp=len(Input)

D={K:V for K,V in enumerate(Input)}
for i in String:
    if i in D:
        Res.append(i)
        
        
# # for i in Input:
# #     if i in String and i not in Res:
# #         Res.append(i)
FinalRes="".join(Res)
print(FinalRes)
# # print(set(FinalRes))
if String in FinalRes:
    print("YES")
# for i in FinalRes:
#     print(i,ord(i),FinalRes.index(i))
    

# D={}
# for K,V in enumerate(Input):
#     print(K,V)
