from collections.abc import Iterable
from typing import Any


# class Test:
#     def __init__(self) -> None:
#         self.a=1
#         self.b=2
    
#     def __str__(self):
#         return f'my class with {self.a} {self.b} {self}'
#         # print(Test)

# obj=Test()
# # print(t.a)
# print(str(obj))
class MyClass:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"MyClass instance with data: {self.data} and memory address: {str(hex(id(self))).upper()}"

obj = MyClass(123)

# Printing the instance using str()
# print(id(obj))
print(obj)
# print(hex(id(obj)))
# class SoftwareEngineering:
#     def __init__(self):
#         self.google="SDE"
#         self.Microsoft="Sr SDE"
#         self.Walmart="SRE II"
#         self.Adobe="Computer Scientist"
#         self.pay="45 LPA"
    
#     def __setattr__(self, name: str, value: Any):
#         if name == "setpay":
#             self.pay="30 LPA"
    
#     def __getattribute__(self, name: str):
#         if name == "salary":
#             return self.google

# SDE = SoftwareEngineering()
# setattr(SDE, "setpay", "55 LPA") 
# print(getattr(SDE,"salary"))

from typing import Any

class SoftwareEngineering:
    
    def __init__(self) -> None:
        self.google = "SDE"
        self.Microsoft = "Sr SDE"
        self.Walmart = "SRE II"
        self.Adobe = "Computer Scientist"
        self.pay = "45 LPA"
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name == "setpay":
            self.pay = "55 LPA"
        else:
            super().__setattr__(name, value)  # Call the superclass method for other attributes
    
    def __getattribute__(self, name: str) -> Any:
        if name == "salary":
            return self.pay
        else:
            return super().__getattribute__(name)  # Call the superclass method for other attributes
    
    def __repr__(self) -> str:
        return f'Ramesh works in Google with Pay of {self.pay}'
    
    def __dir__(self) -> Iterable[str]:
        return ["Google","Microsoft","Adobe","Walmart"]

SDE = SoftwareEngineering()
# SDE.setpay = 5  # Use dot notation to trigger __setattr__
# print(SDE.pay)
# print(dir(SDE))
# print(SDE)
# print(SoftwareEngineering())