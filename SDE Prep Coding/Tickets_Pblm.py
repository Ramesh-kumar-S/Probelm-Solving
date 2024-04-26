tickets = [5,1,1,1]
# tickets = [2,3,2]
k=0
time=0


# for i in range(len(tickets)):
#     if tickets[k] == 0:
#         print(time)
#         break 
#     if tickets[i] == 0:
#         tickets.pop(i)
#     else:
#         tickets[i]-=1
#         time+=1
        
while tickets[k] != 0:
    for i in range(len(tickets)):
        if tickets[i] == 0:
            continue 
        if tickets[k] == 0:
            break
        tickets[i]-=1
        time+=1
#         if tickets[i] == 0:
#             continue 
#         tickets[i]-=1
#         time+=1
    
# for i in range(len(tickets)):
#     if tickets[i] == 0:
#         tickets.pop(i)
    



# while tickets[k] != 0:
#     for per in range(len(tickets)):
#         tickets[per] -= 1
#         if tickets[per] == 0:
#             continue 
# #             tickets.pop(tickets[per])
#         time+=1
        
print(time)
