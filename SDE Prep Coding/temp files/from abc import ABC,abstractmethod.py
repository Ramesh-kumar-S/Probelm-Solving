from abc import ABC,abstractmethod
class SoftwareEngineer:
    print("SDE")
    def __init__(self,name,orgn) -> None:
        self.name=name
        self.orgn=orgn
    
    def __str__(self):
        return f"{self.name} has been selected as an Software Engineer at {self.orgn}."

    def Expertise(self):
        pass

class ComputerScientist(SoftwareEngineer):
    print("Computer Scientist")
    def __init__(self, name, orgn, level) -> None:
        super().__init__(name, orgn)
        self.level=level

class SiteReliabilityEngineer(SoftwareEngineer):
    pass

SRE = SiteReliabilityEngineer("Ramesh Kumar Sekar","Google")
# print(issubclass(SiteReliabilityEngineer, SoftwareEngineer))
# print(isinstance(SRE,SiteReliabilityEngineer))
# print(SRE)
# print(dir(SRE))
# print(SiteReliabilityEngineer.mro())
help(ABC)   