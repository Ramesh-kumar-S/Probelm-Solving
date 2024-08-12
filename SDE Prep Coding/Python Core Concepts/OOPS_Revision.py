#Getter and Setter  -- DONE
#Encapsulation -- Binding Data and Methods together and Hiding the Implementation Details
#Polymorphism -- DONE
#Interfaces  -- DONE

from abc import ABC,abstractmethod
from dataclasses import dataclass
from contextlib import contextmanager

#######################################################
#       Interfaces and Inheritance                    #
#######################################################
class Scientist(ABC):
    
    @staticmethod
    @abstractmethod
    def modifyCompany():
        pass
    
    @classmethod
    @abstractmethod
    def updateExpertise(cls):
        pass
    
class Engineering(Scientist):
    Expertise = "Problem Solving"
    
    def __init__(self, name, role, company) -> None:
        self.name = name 
        self.__role = role
        self.company = company
    
    """
    Getter Method to access the attribute as like an Obj.Attrib 
    rather than as a Instance Method
    """
    @property
    def role(self):
        return self.__role
    
    """
    Setter Method to set/modify the attribute as like an Obj.Attrib 
    rather than as a Instance Method
    """
    @role.setter
    def role(self, newRole):
        self.__role = newRole
    
    """
    Just an utility function that present under class namespace
    Cannot modify Class/Instance attributes
    """
    #Just an Utility function, can't modify any class/instance attributes
    @staticmethod
    def modifyCompany(Orgn):
        company = Orgn
    
    """
    Used to modify the class  level attributes
    """
    #Classmethod - modifies the class level attributes
    @classmethod
    def updateExpertise(cls):
        cls.Expertise = "Computer Scientist"
    
    """
    Used to modify the Instance level attributes
    """
    #Instance Method - modifies the Instance level attributes
    def updateName(self, name):
        self.name = name
        
E = Engineering("Ramesh","SDE", "Google")
print(E.role)

E.role = "Site Reliability Engineer - IBM"
print(E.role) #Site Reliability Engineer - IBM

E.modifyCompany("Nutanix") #Idle call, No functional Impact

Engineering.Expertise #Problem Solving
E.updateExpertise()
Engineering.Expertise #Computer Scientist


#######################################################
#                Polymorphism                         #
#######################################################

"""
Polymorphism in Python allows objects of different classes to be treated as objects of a common superclass. 
It provides a way to perform a single action in different forms. 
Polymorphism is achieved through method overriding and interfaces.

- Compile time Polymorphism (Static Polymorphism)
       A)  The exact method or function that will be invoked is determined by the compiler based on the method signatures, number of arguments, or argument types.
       B)  Eg: Method Overloading, Operator Overloading
- Run time Polymorphism (Dyanmmic Polymorphism)
       A) Run-time polymorphism, also known as dynamic polymorphism, is resolved at runtime rather than at compile time
       B) Eg: Method Overriding, Virtual Functions(C++)
"""
#######################################################
#             Method Overloading                      #
#######################################################
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# Example usage
math_op = MathOperations()

print(math_op.add(5))         # Output: 5
print(math_op.add(5, 10))     # Output: 15
print(math_op.add(5, 10, 15)) # Output: 30

#######################################################
#             Method Overriding                       #
#######################################################
class Engineering(object):
    def getRole(self):
        print("Ramesh - Proficient Engineer")

class SoftwareDeveloper(Engineering):
    def getRole(self):
        print("Ramesh - Software Engineer III - Google")

class SiteReliabilityEngineer(Engineering):
    def getRole(self):
        print("Ramesh - Site Reliability Engineer - Google")

Engineers = [ Engineering(), SoftwareDeveloper(), SiteReliabilityEngineer()]

for Engineer in Engineers:
    Engineer.getRole()
    

#######################################################
# Dataclasss and Context Manager                      #
#######################################################
@dataclass
class SoftwareEngineer(object):
    company : str
    role : str

    @contextmanager
    def getDataStructures(self):
        print("\nProficiency in Data Structures need Sheer amount of Practice !!")
        yield
        print("\t\tArrays, Strings, Stacks, Queues, LinkedList, HashMaps, Tree, Graphs, Heaps\n")
        # yield
    
    def getAlgorithms(self):
        pass
    
S = SoftwareEngineer("Google", "SDE")
with S.getDataStructures() as SMgr:
    print("Data Structures : ")

def YouWillbeAnGoogler():
    pass