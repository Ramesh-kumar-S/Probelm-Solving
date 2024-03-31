UID="B1CDEF2354"
# UID=input()
Validity={}
if len(UID) != 10:
    print("Invalid")
for Char in UID:
    if Char.isnumeric():
        if 'digit' not in Validity:
            Validity['digit'] = 1
        else:
            Validity['digit'] += 1
    if Char.isupper():
        if 'upperCase' not in Validity:
            Validity['upperCase'] = 1
        else:
            Validity['upperCase'] += 1
    if not Char.isalnum():
        if 'alnum' not in Validity:
            Validity['alnum'] = 1
        else:
            Validity['alnum'] += 1
    
Valid=True
# print(len(list(UID)) - len(set(UID)))
if not Validity['upperCase'] >= 2:
    Valid=False
if len(UID) != 10:
    Valid=False
if (len(set(UID)) - len(list(UID)) != 0):
    Valid=False

        
# for _ in range(int(input())):
#     Validity={}
#     UID=input()
#     if len(UID) != 10:
#         print("Invalid")
#     for Char in UID:
#         if Char.isdigit():
#             Validity['Digit'] += 1
        
    