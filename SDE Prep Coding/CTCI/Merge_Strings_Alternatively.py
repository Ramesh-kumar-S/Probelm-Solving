import  itertools

Word1 = "abc"
Word2 = "pqr"

Word1="ab"
Word2="pqrs"

Res=""
for w1,w2 in itertools.zip_longest(Word1, Word2):
    if w1 is None:
        Res+=w2
    if w2 is None:
        Res+=w1
    if w1 and w2 is not None :
        Res+=w1+w2

print(Res)