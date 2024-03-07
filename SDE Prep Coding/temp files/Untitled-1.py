class CutomIteration:
    def __iter__(self) -> None:
        self.val = 10
        return self
    
    def __next__(self):
        if self.val < 100:
            x=self.val
            self.val+=10
            return x
        else:
            raise StopIteration

CustIter = CutomIteration()
iter = iter(CustIter)

print(iter)
for i in iter:
    print(i)


