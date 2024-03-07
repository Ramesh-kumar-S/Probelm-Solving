s="MCMXCIV"
D={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

Vals=[D[x] for x in s ]
M_Index = Vals.index(max(Vals))
print(M_Index)
print(max(Vals))
print(Vals)
Res=0
for i in range(len(Vals)-1):
#     if M_Index == 0 :
#         Res+=D[s[i]]
#         Res = sum(Vals)
# #         return sum(Vals)
#         break 
#     elif M_Index == len(Vals)-1:
#         Res = abs(sum(Vals[:-1])-max(Vals))
# #         return abs(sum(Vals[:-1])-max(Vals))
#         break 
        
            
            
            
    if Vals.index((D[s[i]]))<M_Index:
        Res+=D[s[i]]
    else:
        Res-=D[s[i]]
print(abs(Res))
# for i in range(0,len(s)):
#     if i != len(s)-1:
#         if D[s[i]] < D[s[len(s)-i-1]]:
#             Res += abs(D[s[i]] - D[s[len(s)-i-1]])
#         else:
#             Res+=D[s[i]] + D[s[len(s)-i-1]]
# print(Res)
        
