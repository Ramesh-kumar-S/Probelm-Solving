class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
    
    def __next__(self):
        for outer in self.characters:
            for inner in self.characters:
                return outer+inner
            
    def next(self) -> str:
        for outer in range(len(self.characters)):
            for inner in range(len(self.characters)):
                print(self.characters[outer:inner+4])

    def hasNext(self) -> bool:
        pass
        


# Your CombinationIterator object will be instantiated and called as such:
characters = "abcdef"
combinationLength = 4
obj = CombinationIterator(characters, combinationLength)
# print(obj.next())

# print(param_1)
# param_2 = obj.hasNext()

import random

foo = {'a', 'b', 'c', 'd', 'e'}
print(random.choice(list(foo)))
print(random.choice(list(foo)))
print(random.choice(list(foo)))
