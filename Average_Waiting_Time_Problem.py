customers = [[1,2],[2,5],[4,3]]
# customers = [[5,2],[5,4],[10,3],[20,1]]
Waiting_Delays=[]

CurrentFinishingTime=customers[0][0]
for customer in customers:
    if customer[0] > CurrentFinishingTime:
        CurrentFinishingTime = customer[0]
    Arrival_Time=CurrentFinishingTime
    Waiting_Time=customer[1]
    Finishing_Time=Arrival_Time+Waiting_Time
    print(Arrival_Time, Finishing_Time, Finishing_Time-customer[0])
    Waiting_Delays.append(Finishing_Time-customer[0])
    CurrentFinishingTime=Finishing_Time

print(Waiting_Delays)
Num=sum(Waiting_Delays)/len(Waiting_Delays)
print("{:.5f}".format(Num))

# print((2+6+7)/3)