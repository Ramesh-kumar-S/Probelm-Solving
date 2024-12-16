# nums = [1,0,-1,0,-2,2]
# target = 0
# Complement = {}
# for i in nums:
#     pass


class CustomIter(object):
    def __init__(self, end, start=0) -> None:
        if not start:
            self.current = 0
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            current = self.current
            self.current += 5
            return current


class Fibonacci:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current_count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count >= self.max_count:
            raise StopIteration  # Stop after generating max_count numbers
        self.current_count += 1
        a = self.a
        self.a, self.b = self.b, self.a + self.b
        return a
            
C = CustomIter(100)
# print(next(C))
# print(next(C))
# print(next(C))
# print(next(C))
# print(next(C))
# print(next(C))
# print("-------")
# for i in C:
#     print(i)

F = Fibonacci(10)
# print(next(F))
# for i in F:
#     print(i)


import re
input = "#F0A1FB"
input = "#fffabg"
pattern = r'^#[a-fA-F0-9]{3}$|^#[a-fA-F0-9]{6}$'
print(re.findall(pattern, input))
if re.match(pattern, input):
    print("Matched")
else:
    print("No Match")