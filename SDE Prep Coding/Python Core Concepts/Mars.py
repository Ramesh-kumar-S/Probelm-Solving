Expected="OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS"
Original="SOS"*(len(Expected)//3)

Count=0
for E,O in zip(Expected,Original):
    if E != O:
        Count+=1

print(Count)
