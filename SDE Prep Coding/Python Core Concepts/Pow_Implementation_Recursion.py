N=5

def Pow(Value, power):  # sourcery skip: assign-if-exp
    # return 1 if power == 0 else (N*Pow(N,power-1))
    print(Value, power)
    if power in [0, 1]:
        return 1
    if power < 0:
        
    else:
        return (Value*Pow(Value,power-1))

print(Pow(2.0000,-2))
