#Python program to get the binary Number without bin Function
Num=26
Num=2147483645

def getBaseValue(Num,Base):
    Value=Num
    Binary=[]
    while Num > 0:
        Remainder = Num%Base
        Binary.append(Remainder)
        Num //= Base
        # print(Num,Remainder)

    Binary=reversed(Binary)
    Result="".join(map(str,Binary))
    print(f'\nBase {Base} equivalent of the {Value} is  {Result}')
    return Result

Res=getBaseValue(Num,2)
print(str(Res).count("1"))