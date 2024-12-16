"""
name1 = abc
name2 = acbdh

-Remove common characters
-Get the remaining characters count
-count the remaining char count on FLAMES
-remove the respective word
-Once the FLAMES reaches the word length to 1, Print the Result
"""
Flames = list("FLAMES")
Name1 = "asd"
Name2 = "abcd"

Non_Common_Elements = set(Name1).symmetric_difference(set(Name2))
Length = len(Non_Common_Elements)

while len(Flames) != 1:
    Count = 0
    for i in Flames:
        if Count == Length-1:
            Last_Pop_Index = Flames.pop(Flames.index(i))
            Count = 0
            break
        Count += 1


# from datetime import datetime
# print(datetime.today().time())
