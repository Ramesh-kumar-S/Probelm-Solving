class Google:
    def __init__(self, Role) -> None:
        self.Role = Role
    
    def __repr__(self) -> str:
        return f'Google({self.Role!r})'
    
G1 = Google("Software Engineer III")

#Recreate the G1 Object using Repr
Repr_G1=repr(G1)
G2 = eval(Repr_G1)
print(G2)