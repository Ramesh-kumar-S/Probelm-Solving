class Queue(object):
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, value):
        self.queue.insert(0, value)
    
    def deque(self):
        self.queue.pop(0)
    
    #Custom dunder method
    def __len__(self):
        return len(self.queue)
    
    def __str__(self) -> str:
        return str(self.queue)
    
    def __test__(self):
        for elem in self.queue:
            print(elem)

t = Queue()

for i in range(6,  0, -1):
    t.enqueue(i)
    
def test(obj):
    if hasattr(obj, "__test__"):
        return obj.__test__()

print(t)
print(len(t))
print()
test(t)

# for i in range(10,0, -1):
#     print(i)