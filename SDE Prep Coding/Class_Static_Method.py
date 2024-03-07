import os
os.system("cls")

class SoftwareEngineering:

    def __init__(self,role,expertise) -> None:
        self.role=role
        self.expertise = expertise
        print(f'Ramesh is an {self.role} and Expertised in {self.expertise}')
        
    @staticmethod
    def Role():
        print("Ramesh is an Software Engineer")
        return

    @classmethod
    def ActualExpertise(cls):
        print("Calling from Class Method Decorator")
        return cls("Computer Scientist","Algorithmic Thinking")
    
    def isHavingRole(self):
        if hasattr(self,'role'):
            print(f'Yes, Ramesh is an {self.role}')
    
    def __del__(self):
        print("Destructor is called")
        
    print("END")

SE = SoftwareEngineering("SDE","Python")
SE.Role()
del SE
# SE.ActualExpertise()
# SE = SoftwareEngineering("Computer Scientist","Algorithmic Thinking")
# SE.isHavingRole()
# del SE
# SoftwareEngineering.isHavingRole()
# SoftwareEngineering.isHavingRole()
# A.ActualExpertise()