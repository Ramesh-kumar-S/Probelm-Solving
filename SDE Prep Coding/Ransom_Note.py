from collections import  Counter

# magazine = "ab"
# ransom = "aa"

# def ransomNote(ransomNote: str, magazine: str) -> bool:
#     magazineCount = Counter(magazine)
#     for char in ransom:
#         if char  in magazineCount:
#             if ransom.count(char) >= magazineCount[char]:
#                 magazineCount[char] -=1  #Decrement the Magazine count once char is used for Ransom
#             else:
#                 return False 
#         else:
#             return False
#     return True
            
# #     for char in ransom:
# #         if ransom.count(char) >= magazineCount[char]:
# #             return False 
# #     return True

# magazine = "aa"
# ransom = "aab"
# print(ransomNote(ransom, magazine))
# from collections import Counter

MagMap = {}
magazine = "two times three is not four"
note = "two times two is four"

magazine = "give me one grand today night"
note = "give one grand today"

for word in magazine:
    if word not in MagMap:
        MagMap[word] = 1
    else:
        MagMap[word] += 1

def ransome():
    for word in note:
        if word in MagMap  and MagMap[word] > 0:
            MagMap[word] -= 1
        else:
            return False
    return True

print(ransome())