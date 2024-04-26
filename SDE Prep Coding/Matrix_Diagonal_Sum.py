mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
Result=0
for X in range(len(mat)):
    Result+=mat[X][X]+mat[X][len(mat)-X-1]
if len(mat)%2 == 1:
    Result-=mat[len(mat)//2][len(mat)//2]
print(Result)

# PD=[]
# SD=[]
# for Num in range(len(mat)):
#     PD.append(mat[Num][Num])

# for Num in range(len(mat)):
#     SD.append(mat[Num][len(mat)-Num-1])

# if len(mat)%2 == 0:
#     return sum(PD)+sum(SD)
# else:
#     return sum(PD)+sum(SD)-mat[len(mat)//2][len(mat)//2]
        
