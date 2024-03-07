
#hasattr
#isinstance()
#type(obj)
#Creating an Class
class SDE:
    
    @staticmethod
    def SoftwareDevelopment():
        SDE="Ramesh Kumar Sekar - SDE"
        return SDE

    @classmethod
    def ComputerScientist(cls):
        CS="ComputerScientist"
        return CS
    
S=SDE()
# print(SDE.SoftwareDevelopment())
# print(SDE.ComputerScientist())
# print(S.__str__())

class Powercycle():
    
    Provider ="Raritan"
    
    def __init__(self,A,B,IP):
        self.A=A
        self.B=B
        self.IP=IP
        
    def getOutlets(self):
        print(self.A)
        print(self.B)
        print(self.IP)
        
    def setProvider(self):
        Provider = "Rariton Corp"
        raise ValueError(f'{Provider} is an PDU Provider')
    
    def getCred(self):
        self.user="admin"
        self._passwd="nbv12345"
        return self._passwd
    
    def isPasswdSet(self):
        if hasattr(self,"IP"):
            print("Passwd Set")
        else:
            print("No Man")
    
P1=Powercycle(10,15,"10.127.56.65")
# print(P1)
# P1.getOutlets()
# P1.isPasswdSet()
# print(P1.getCred())
# print(Powercycle.Provider)
# print(P1.setProvider())
# print(Powercycle.Provider)

# print(A)

# print(P1)
# print(type(P1))
# print(isinstance(P1,Powercycle))


class DevOps:
    Role = "( Software Engineer - DevOps )"
    Programming ="Python , Bash "
    
    @classmethod
    def getRole(self):
        return  "Ramesh Kumar Sekar - ",self.Role
    
    @staticmethod    
    def getProgramming():
        return "Programming Expertise : ",DevOps.Programming
    

def Vision():
    return "A Top Notch Software Engineer"

Dev=DevOps()
print(DevOps.getRole())
print(DevOps.getProgramming())
