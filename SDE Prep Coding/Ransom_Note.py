from collections import  Counter

# magazine = "ab"
# ransom = "aa"

def ransomNote(ransomNote: str, magazine: str) -> bool:
    magazineCount = Counter(magazine)
    for char in ransom:
        if char  in magazineCount:
            if ransom.count(char) >= magazineCount[char]:
                magazineCount[char] -=1  #Decrement the Magazine count once char is used for Ransom
            else:
                return False 
        else:
            return False
    return True
            
#     for char in ransom:
#         if ransom.count(char) >= magazineCount[char]:
#             return False 
#     return True

magazine = "aa"
ransom = "aab"
print(ransomNote(ransom, magazine))
