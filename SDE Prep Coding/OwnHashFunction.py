def HashFunction(str):
    #Blue -> B-ASCII Value, L-ASCII Value etc,.
    Ascii_Mapping={K:ord(K) for K in str}
    Ascii_sum=sum(Ascii_Mapping.values())
    Index_val=Ascii_sum % 4
    print(Ascii_Mapping,Ascii_sum,Index_val)
    
HashFunction("Environmental")
































