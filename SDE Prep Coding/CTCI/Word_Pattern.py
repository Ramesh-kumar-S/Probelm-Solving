from collections import OrderedDict
import sys

pattern="abba"
s="dog cat cat fish"

D=OrderedDict()
for i in zip(list(pattern), s.split()):
    if i[0] in D.values():
        print(False)
        raise SystemExit
    D[i[1]]=i[0]
    
print(D['fish'])
Result=""
for String in s.split():
    if String in D:
        Result+=D[String]

print(Result == pattern)