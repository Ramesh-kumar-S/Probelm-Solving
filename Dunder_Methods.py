class String(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    # def __getattribute__(self, name ):
    #     print(f'__getAttribute__ is called for {name}')
    #     return super(String,self).__getattribute__(name)
    
    # def __setattr__(self,name,value):
    #     print(f'__setattr__ is called for {name}')
    #     if hasattr(self,"a"):
    #         self.a=value+10
    #         return super().__setattr__(name,value)
            
    def __add__(self,Value):
        return self.a+self.b+Value
      
    def __repr__(self):
        return f'A : {self.a} ,B: {self.b}'
    
    def __call__(self, a, b):
        self.a=a
        self.b=b
    
    #Gets Called If the Attribute doesn't Exist in a Class
    def __getattr__(self,name):
        return f'Bruh !! The Attrib data {name} doesn\'t Exist ;)'

S=String(2,6)
print(S.G)
#Callable Object
print(S)
# S(5,5)  #Callable Object & Modifying the Attributes of Class Just Like an Function
# print(S)

#Operator Overloading 
# print(S + 5)

#######################################################################################################################################
#                                                           DATA ClASSES                                                              #
#######################################################################################################################################
from dataclasses import dataclass,field


def Version_Parser():
    return "0312A"

@dataclass(frozen=True)   #Attributes inside the Class Become Immutable(Can't be modified inside and outside the Class)
class Build:
    Build_Type : str = "Sam_Build"
    Build_Branch : str = "Rel/KBMR2"
    Build_version : str = field(default_factory=Version_Parser)
    Repo : str = "Pre-Built Repo"
    
    # def __post_init__(self):
    #     if hasattr(self,"Build_Type"):
    #         if self.Build_Type == "Sam_Build":
    #             self.Repo = "Pre-Built Repo"
    #         else:
    #             self.Repo = "Fresh Repo"
                
    
    
B=Build()   
# B=Build("Sam_Build", "KB")
# B1=Build("Sam Build","0312","KBMR2")

# print(B.Build_version)  #Object can be accessed as if its a Normal Class 
# print(B.Build_Branch)
# print(B.Repo)
# print(B)

#Data Classes has builtin Automated Magic/Dunder Methods
# print(B)  #__repr__  Dunder/Magic Methods  

# print(B==B1)  #__eq__ Dunder/Magic Methods

#Using Post Init Method to Initialize Attribute's soon after Built in __Init__ Method Intialization.
# print(B.Repo)