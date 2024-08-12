# a=[1,2,2,1,1,3,5,1,4,4]

# D={1:0,2:0,3:0,4:0,5:0}

# for i in a:
#     if i in D:
#         D[i] +=1
# print(D)

# import string
# alphabet = set(string.ascii_lowercase)
# a="The quick brown fox jumped over the lazy dog."
# # a="The five boxing wizards jump quickly"

# def check_string(my_string):
#     Missing=[]
#     alphabet = set(string.ascii_lowercase)
#     alpha="abcdefghijklmnopqrstuvwxyz"
#     for X in alpha:
#         if X not in my_string.lower():
#             Missing.append(X)
#     print("".join(Missing))


# class Item:
#     def __init__(self,item_type,price):
#         self.item_type=item_type
#         self._price=price

# class Cake(Item):
#     def __init__(self, item_type, price, slices):
#         super().__init__(item_type,price)
#         self.slices = slices
    
#     #Getter Method for Protected Attribute  
#     @property
#     def price(self):
#         return self._price

# spice_cake = Cake("spice", 18, 8)
# chocolate_cake = Cake("chocolate", 24, 6)


# result = False
# try:
#     # Attempt to set the price attribute.
#     # spice_cake.price = 18
#     spice_cake.price = 200
# except AttributeError:
#     # Return True if the price attribute cannot be set.
#     result = True
    
# print(result)


def LogDeco(func):
    def Log():
        print("+","-"*10,"+")
        print("|"," "*10,"|")
        res=func()
        print(res)
        print("|"," "*10,"|")
        print("+","-"*10,"+")
        return res
    return Log

from functools import wraps
from time import perf_counter
from typing import Any

def Bold(func):
    @wraps(func)
    def addBold():
        res="<b>" + func() + "</b>"
        # res=func()
        # print(res,end="")
        # print("</b>",end="")
        return res
    return addBold

def Italic(func):
    @wraps(func)
    def addItalic():
        res="<i>" + func() +"</i>"
        # print("<i>",end="")
        # res=func()
        # print(res,end="")
        # print("</i>",end="")
        return res
    return addItalic

# @LogDeco
# def SendJsonData():
#     return "  Fibonacci"

def Munch(start,end):
    def do_munch(func):
        @wraps(func)
        def MunchWrapper():
            res=func()
            return res[:start]+(end-1)*"X"+res[end:]
        return MunchWrapper
    return do_munch

# @Bold
# @Italic
# start=perf_counter()
@Munch(1,6)
def Fibonacci():
    return "Fibonacci"
# end=perf_counter()
# print(f'{start-end:.5f}s')
print(Fibonacci())

# SendJsonData=LogDeco(SendJsonData)
# SendJsonData()

def Function():
    """
    Function to test the DocString
    """
    help(Function)    #Print the DocString
    print(Function.__doc__)  #Print the DocString
    print(Function.__name__)   #Print the Function Name
    print(Function.__qualname__) #Print the Function Name

# Function()
# print(help(Function))

class Call:
    def __init__(self) -> None:
        pass
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Call Dunder has been called.")
    
    def __repr__(self) -> str:
        print("Class Instance can be printed")
        
# c=Call()
# c()
# print(c)