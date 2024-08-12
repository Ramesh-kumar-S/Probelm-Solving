"""
- Factory method is an creational type design pattern, which focus on Object creation
- Provides Flexibility
- Example of Run-time/Dynamic Polymorphism (Method Overriding )
"""
from abc import ABC, abstractmethod

class Engineer(ABC):
    def __init__(self, Role) -> None:
        self.Role = Role
    
    @abstractmethod
    def getRole(self):
        pass

class SDE(Engineer):
    def __init__(self, Role) -> None:
        super().__init__(Role)
    
    def getRole(self):
        return f"Ramesh is an Brilliant & Proficient {self.Role} - || Google/Apple has ever seen!!"

class SRE(Engineer):
    def __init__(self, Role) -> None:
        super().__init__(Role)
    
    def getRole(self):
        return f"Ramesh is an Brilliant & Proficient {self.Role} @ (Walmart, Google, NetApp)"

def getEngineerProgrammer(Engineer="SDE"):
    Expertise = dict(SRE=SRE("Site Reliability Engineer"),
                     SDE=SDE("Software Development Engineer"))
    return Expertise[Engineer]

S1 = getEngineerProgrammer("SRE")
print(S1.getRole())

S2 = getEngineerProgrammer()
print(S2.getRole())