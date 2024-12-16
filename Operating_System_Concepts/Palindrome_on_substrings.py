def isPalindrome(s):
    return s == s[::-1]

def getPalindromicSubstrings(String):
    Palindromes = []
    length = len(String)
    
    for i in range(length):
        for j in range(i+1, length+1):
            if isPalindrome(String[i:j]):
                Palindromes.append(String[i:j])    
    return Palindromes

print(getPalindromicSubstrings("babad"))