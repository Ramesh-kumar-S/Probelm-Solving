"""
- Abstract Factory method builds on Factory method
- Factory method will return a Single Object, Abstract Factory Method will return a family of Objects
- Will yields a family of Objects
- Abstract Factory (Pet Factory) -> Concrete Factory (Dog Factory) -> Concrete Product ( Dog, Dog_Food)
"""
from abc import ABC, abstractmethod

class EngineerFactory(object):
    def __init__(self, EngDomain) -> None:
        self.__EngDomain = EngDomain
    
    def getDomainExpertise(self):
        print(
            'Finally the Name is Ramesh Kumar Sekar - Boss of Software Engineering!!'
            )
        SREConcrete = self.__EngDomain.getSoftwareEngineer()
        SREConcrete.expertise()
        
# class SDE:
#     def expertise(self):
#         print(f'Ramesh is an Brilliant SDE @ {self.company} handling critical Software Design Issues')

# class SE:
#     def expertise(self):
#         print(f'Ramesh is an Proficient SE @ {self.company} mainting an Highly Resilient Archeitecture')
        
class SoftwareDevelopment:
    def __init__(self, company) -> None:
        self.company = company
    
    def getSDE(self):
        return SDE()

    def getSoftwareEngineer(self):
        return SE()
        
class SDE:

    def expertise(self):
        print('Ramesh is an Brilliant SDE @ Google handling critical Software Design Issues')

class SE:
    
    def expertise(self):
        print('Ramesh is an Proficient SE @ Google maintaining an Highly Resilient Archeitecture')

SDEFactory = SoftwareDevelopment("Google")

EngFactory = EngineerFactory(SDEFactory)
EngFactory.getDomainExpertise()
