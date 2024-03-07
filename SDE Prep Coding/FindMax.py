List=[5,9,13,6,9,3,1]
Max=List[0]
Min=List[0]
# for i in List:
#     if i>Max:
#         Max=i
#     elif i<Min:
#         Min=i

for i in List:
    if i>Max:
        Max=i
    # if i<Min:
    #     Min=i
    else:
        Min=i
    print(Max,Min)

print("Maximum Value is ",Max,"\nMinimum Value is ",Min)
