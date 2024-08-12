# try:
#     a=1
# except Exception:
#     print("Exception")
# else:
#     print("Ramesh - SDE")
    
class ControllerFailure(Exception):
    def __init__(self, ControllerType, Failure, ReturnCode) -> None:
        self.ControllerType = ControllerType
        self.Failure = Failure
        self.ReturnCode = ReturnCode
    
    def __str__(self) -> str:
        return f'{self.ControllerType} Controller has been failed due to {self.Failure} with error code as {self.ReturnCode}'
    
class DriveFailure(Exception):
    def __init__(self, DriveType, Failure, ReturnCode) -> None:
        self.DriveType = DriveType
        self.Failure = Failure
        self.ReturnCode = ReturnCode
    
    def __str__(self) -> str:
        return f'{self.DriveType} Drive has been failed due to {self.Failure} with error code as {self.ReturnCode}'
    
def Component_Failure(Comp):
    if Comp == "Controller":
        raise ControllerFailure("SAS", "Update-Failure", "265")
    elif Comp == "Disk":
        # raise Exception("Ramesh Kumar - Software Engineer (Google)")
        raise DriveFailure("U.3 SAS4", "SelfTestFailed", "265")
   
try:
    Component_Failure("Disk")
except ControllerFailure as e:
    print(f"Controller Failure : {e}")
except DriveFailure as e:
    print(f"Disk Failure : {e}")
except Exception as e:
    print(e)
else:
    print("Storage Component Update Success")


