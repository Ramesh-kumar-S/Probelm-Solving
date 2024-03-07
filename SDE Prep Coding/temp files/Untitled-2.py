class ComputerScientist:
#     def __new__(cls):
#         print("Hey Ramesh is an Computer Scientist and \
# have Super Quick probelm Solving Skills!")
        
    
    Role="Software Engineer"
    def __init__(self) -> None:
        self.a = 40
        self.__b = 50
    
    def getB(self):
        return self.__b
class SDE(ComputerScientist):
    pass

CS = ComputerScientist()
print(CS._ComputerScientist__b)
Ramesh_Scientist = ComputerScientist()
print(ComputerScientist.Role)
# print(SDE.mro())
# print(Ramesh_Scientist.getB())

print(SDE.__mro__)

# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]

# dictionar = {K:V[0] for K,V in zip(number,months) }
# print(dictionar)


