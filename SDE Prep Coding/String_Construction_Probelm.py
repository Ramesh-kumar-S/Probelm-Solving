#Hackerrank String Construction Probelm

# A="abcd"
A="abab"
B=""
Cost=0
for i in A:
    print(i)
    if i not in B:
        B+=i
        Cost+=1
    else:
        B+=i
        
    # B+=i
    # if B in A:
    #     print(B,"Yes")