String = "A man, a plan, a canal: Panama"
String = "0P"

New_String="".join([x.lower() for x in String if x.isalnum()])
print(New_String)
print(New_String[::-1])