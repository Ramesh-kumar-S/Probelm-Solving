strs = ["eat","tea","tan","ate","nat","bat"]
strs = "a"
Anagram = {}

count=0
for word in strs:
    sorted_word="".join(sorted(word))
    if sorted_word in Anagram:
        Anagram[sorted_word].append(word)
    else:
        Anagram[sorted_word] = [word]
    
print(list(Anagram.values()))
        