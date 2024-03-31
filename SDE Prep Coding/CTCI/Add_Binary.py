def addBinary(a: str, b: str) -> str:
    Result=bin(int(a,2)+int(b,2))[2:]
    return Result

print(addBinary("11","1"))

