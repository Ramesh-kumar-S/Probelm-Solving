class Employee(object):
    def __init__(self, name, phone) -> None:
        if not isinstance(name, str):
            raise ValueError("Invalid Data Type Passed for Name")
        else:
            self.name = name

        if not isinstance(phone, int):
            raise ValueError("Invalid Data Type Passed for Phone No")
        else:
            self.phone = phone
        
        
    #     self.phone = phone
    #     self.salary = salary
    
    # @property.getter
    # def name(self):
    #     return self.name
    
    # @property.setter
    # def name(self, EmployeeName):
    #     if not isinstance(Employee, str):
    #         raise ValueError("Invalid Data Type Passed")
    #     else:
    #         self.name = EmployeeName            

try:
    E=Employee(1234556, "Hello")
except ValueError as e:
    print("Exception has been raised : {}".format(e))
# print(E.name)
# print(E.phone)

count "Ramesh" filename.txt

grep -wi "Ramesh" filename.txt