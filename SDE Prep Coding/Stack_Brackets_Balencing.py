def isBalanced(s):
    Map = {")": "(", "]": "[", "}": "{"}
    Stack = []
    for char in s:
        if char in Map:
            if Stack and Stack[-1] == Map[char]:
                Stack.pop()
            else:
                return "NO"
        else:
            Stack.append(char)
            
    return "YES" if not Stack else  "NO"  
    # Write your code here
isBalanced("{[()]}")

A="{[(])}"
is_Balenced =True
Openers = []

# D={"{":"}","(":")","[":"]"}
# Res=list(A)
# for X in range(len(list(A))//2):
#     print(Res[X])
# D={"{":"}","(":")","[":"]"}
# for opener in A:
#     if opener == "{" or opener == "[" or opener == "(" :
#         Openers.append(opener)

# for i in A:
#     print(i)


# print(Openers)
# for i in Openers:
#     print(i)

# A()
# print(andi)

#     if i != Count:
#         if LHS != A[i] and RHS != A[len(A)-1-i]:
#             is_Balenced = False
#         # print(LHS,RHS)
#         # # if LHS != RHS:
#         # # if A[i] != A[len(A)-1-i]:
#         # #     is_Balenced = False
#     else:
#         break
# print(is_Balenced)






















