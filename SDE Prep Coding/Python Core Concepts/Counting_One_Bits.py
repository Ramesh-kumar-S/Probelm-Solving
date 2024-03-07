#Counting No of 1's in Bits
N=5
Num_Bits=[]
for i in range(N+1):
    Num_Bits.append(str(bin(i)).count("1"))
    
print(Num_Bits)
    