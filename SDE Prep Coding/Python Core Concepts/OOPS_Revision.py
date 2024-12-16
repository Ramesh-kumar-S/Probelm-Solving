
# todo : Getter and Setter -- DONE
# todo : Encapsulation -- Binding Data and Methods together and Hiding the Implementation Details
# todo : Polymorphism -- DONE
# todo: Interfaces  -- DONE

from functools import singledispatch
from abc import ABC, abstractmethod
from dataclasses import dataclass
from contextlib import contextmanager
from typing import Any


class Google_SDE(object):
    pass


R = Google_SDE()
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
    # Just an Utility function, can't modify any class/instance attributes
    @staticmethod
    def modifyCompany(Orgn):
        company = Orgn

    """
    Used to modify the class  level attributes
    """
    # Classmethod - modifies the class level attributes
    @classmethod
    def updateExpertise(cls):
        cls.Expertise = "Computer Scientist"

    """
    Used to modify the Instance level attributes
    """
    # Instance Method - modifies the Instance level attributes

    def updateName(self, name):
        self.name = name


E = Engineering("Ramesh", "SDE", "Google")
print(E.role)

E.role = "Site Reliability Engineer - IBM"
print(E.role)  # Site Reliability Engineer - IBM

E.modifyCompany("Nutanix")  # Idle call, No functional Impact

Engineering.Expertise  # Problem Solving
E.updateExpertise()
Engineering.Expertise  # Computer Scientist


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
print(math_op.add(5, 10, 15))  # Output: 30

# ??????????????????????????????????????????????????
# ? Method Overloading using Functools dispatch    ?
# ??????????????????????????????????????????????????

from functools import singledispatch

@singledispatch
def RameshGoogler(arg):
    print("Default Implementation is called")


@RameshGoogler.register(str)
def getGoogleRole(arg):
    print("Ramesh - Google From Str Implementation")


@RameshGoogler.register(int)
def getGooglePackage(arg):
    print("Ramesh - Google From INT Implementation")


# * Same Function with different datatypes, Respective calls will be accordingly
RameshGoogler(1)
RameshGoogler("Hello")
RameshGoogler(9.8)

# * dispatch(data type) - Display mapping between the functions as with their respective datatypes

# print(RameshGoogler.dispatch(int))
# print(RameshGoogler.dispatch(str))
# print(RameshGoogler.dispatch(float))

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


Engineers = [Engineering(), SoftwareDeveloper(), SiteReliabilityEngineer()]

for Engineer in Engineers:
    Engineer.getRole()


#######################################################
# Dataclasss and Context Manager                      #
#######################################################
@dataclass
class SoftwareEngineer(object):
    company: str
    role: str

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

##############################################################
#          __Slot__ Method(Memory Optimizationn)             #
##############################################################
"""
Ideally python stores all of the attributes in the Object's Dictionary (obj.__dict__), which is makes creation/retreival/deletion easier
But at the cost of Memory Overhead, which is why __slots__ need to be utilized.

- Attributes Should be decalred  as list before Initialisation on Initializer 
- No dynammic attributes allocation is allowed
- Class which inherits must also use __Slots__ functionality.
"""
class Engineer(object):
    __slots__ = ["Name", "Role", "Company", "Expertise"]
    
    def __init__(self) -> None:
        self.Name = "Ramesh Kumar Sekar"
        self.Company = "Google Inc"
        self.Role = "Software Engineer"
        self.Expertise ="Software Design, Problem Solving"
    
    def __str__(self) -> str:
        return f'Congratulations  {self.Name}!! You\'ve been selected as an {self.Role}-|| @ {self.Company}, We would be honored you to bring {self.Expertise} to Google'
        
    def __call__(self, *args: any, **kwds: any) -> any:
        return args

Eng = Engineer()
print(Eng)   #__str__ dunder method will be Invoked

print(Eng("Ramesh", "Google")) #__call__ dunder method will be Invoked


#####################################################
#           Aggregation                             #
#####################################################
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

# Creating book instances
book1 = Book("The Catcher in the Rye")
book2 = Book("To Kill a Mockingbird")

# Creating a library and adding books to it
library = Library()
library.add_book(book1)
library.add_book(book2)

# The books exist independently of the library
print(book1.title)  # Outputs: The Catcher in the Rye

# Deleting the library does not delete the books
del library
print(book1.title)  # Still outputs: The Catcher in the Rye

#####################################################
#           Composition                             #
#####################################################
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, horsepower):
        self.engine = Engine(horsepower)  # Engine is created within Car and owned by Car

# Creating a Car instance with an Engine
my_car = Car(150)

# Accessing the engine's horsepower
print(my_car.engine.horsepower)  # Outputs: 150

# Deleting the car also deletes the engine
del my_car
# Now my_car.engine would not be accessible since my_car is deleted.