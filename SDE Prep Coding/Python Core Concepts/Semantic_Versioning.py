import sys
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        Result = 0
        V1=[x for x in version1.split(".")] 
        V2=[x for x in version2.split(".")] 
        
        def ConvertToFloat(x):
            if x != "":
                return float(x)
            
        V1=list(map(ConvertToFloat,V1))
        V2=list(map(ConvertToFloat,V2))
    
        def Major(V1,V2):
            if V1[0] > V2[0]:
                Major=1
            elif V1[0] == V2[0]:
                Major=0
            else:
                Major=-1
            return Major

        def Minor(V1,V2):
            if len(V1) == 1:    
                V1.append(0)
            if len(V2) == 1:
                V2.append(0)
                
            if V1[1] > V2[1]:
                Minor=1
            elif V1[1] == V2[1]:
                Minor=0
            else:
                Minor=-1
            return Minor

        def Patch(V1,V2):
            if len(V1) == 2:    
                V1.append(0)
            if len(V2) == 2:
                V2.append(0)
                
            if V1[2] > V2[2]:
                Patch=1
            elif V1[2] == V2[2]:
                Patch=0
            else:
                Patch=-1
            return Patch

        def Incremental(V1,V2):
            if V1[3] > V2[3]:
                Inc = 1
            elif V1[3] == V1[3]:
                Inc = 0
            else:
                Inc = -1
            return Inc
        
        Major_Val = Major(V1,V2) 
        Minor_Val = Minor(V1,V2)
        Patch_Val = Patch(V1,V2)
        
        if Major_Val == 0:
            if Minor_Val == 0:
                if Patch_Val == 0:
                    if len(V1) == 4 or len(V2) == 4:
                        Result = Incremental(V1,V2))
                else:
        
                    Result = Patch_Val
            else:
                Result = Minor_Val
        else:
            Result = Major_Val

        return Result

S = Solution()
print(S.compareVersion("3.0.4.10", "3.0.4.2"))




