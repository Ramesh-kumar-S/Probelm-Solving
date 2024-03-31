Arr =  [1, 3, 3, 4]
Target = 5

Difference = {}
for Index,Val in enumerate(Arr):
    Complement = Target - Val
    
    if Complement in Difference:
        print(sorted([Index,Difference[Complement]]))
    
    Difference[Val] = Index
    