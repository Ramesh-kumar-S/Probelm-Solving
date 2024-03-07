
class Ramesh:
    
    def __init__(self,profession):
        self.profession=profession
        print(f"Ramesh is an World-class {self.profession }")
    
    def display(self):
        return self.profession
        
R=Ramesh("SDE-II")
A=R.display()
CM=classmethod()
print(A)