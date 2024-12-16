a="abba"
SubStr = []
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        if a[i:j] not in SubStr:
            SubStr.append(a[i:j])

print(SubStr)
for str in SubStr:
    print(str, str[::-1])
    # if str == str[::-1]:
    #     print(str, str[::-1])
    
    