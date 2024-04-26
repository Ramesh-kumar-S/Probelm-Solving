from collections import  Counter
string = "aaabccddd"
string = "tmubonuhlaryejgftedrhmdxrplneqpwhsketqicdpqlecluydmgykrubgmpwfqviabkjoiqdftgidmgrdbk"
stack = list(string)

Reduced = [x for x,y in sorted(Counter(stack).items()) if y%2 != 0]
print("".join(Reduced))
# Res = ""
# for i in range(0,len(string)-1,2):
# #     print(stack[i],stack[i+1])
#     print(i,i+1)
# #     i+=2
