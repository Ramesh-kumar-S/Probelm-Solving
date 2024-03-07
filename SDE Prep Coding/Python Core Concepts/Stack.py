def Push(Array,item):
    #Adding a Item to Top of the stack
    Array.insert(0,item)
    print(Array)

def Pop(Array):
    #Popping the item from the stack
    top=Array.pop()
    return top

def Peek(Array):
    top=Array[-1]
    return top

Arr=[5,7,8,9]
Push(Arr,4)
Push(Arr,3)

Popped_item=Pop(Arr)
print(f"{Popped_item} is Popped from the Array")

Popped_item=Pop(Arr)
print(f"{Popped_item} is Popped from the Array")

top_item=Peek(Arr)
print(f"{top_item} is top from the Array")

