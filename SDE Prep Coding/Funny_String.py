String = "bcxz"
Reversed_String = String[::-1]

Str_Ascii = [ord(X) for X in String]
Rev_Ascii = [ord(X) for X in Reversed_String]

Abs_Str_Ascii = [abs(Str_Ascii[N]-Str_Ascii[N+1]) for N in range(len(Str_Ascii)-1)]
Abs_Rev_Ascii = [abs(Rev_Ascii[N]-Rev_Ascii[N+1]) for N in range(len(Rev_Ascii)-1)]


if Abs_Str_Ascii == Abs_Rev_Ascii:
    print("Funny")
else:
    print("Not Funny")
    
    
    
    