lookupTable = {}
Str = "https://leetcode.com/problems/design-tinyurl"
# Str = "http://www.leetcode.com/faq/?id=10"


#parsing the last 7 characters and
#Converting to Ascii values
#Store it back on lookupTable
Ascii = [ord(x)+2 for x in Str.split(".com")[-1]] 
Decoded_Ascii = [chr(x-2) for x in Ascii]
print("".join(Decoded_Ascii))

shortenedUrl = "".join(Decoded_Ascii)
print(f'http://tinyurl.com/{shortenedUrl}')

lookupTable[shortenedUrl] = Str

print(lookupTable)

import math
print(math.factorial(7))
# 
# print("http://tinyurl.com/tinyurl".split("/")[-1])
# print("http://www.leetcode.com/faq/?id=10"[-7:])