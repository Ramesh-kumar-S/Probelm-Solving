from collections import deque
N=int(input())
Deq=deque()
for query in range(N):
    query_input=input()
    if int(query_input.split()[0]) == 1:
        Deq.append(int(query_input.split()[1]))
    elif int(query_input.split()[0]) == 2:
        Deq.popleft()
    elif int(query_input.split()[0]) == 3:
        print(Deq[0])
    

# print(Deq)
