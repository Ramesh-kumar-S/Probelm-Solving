#### Custom Doc String 
def MyFunction(N1 : int, N2: int) -> None:
    """
    MyFunction(N1,N2)  -- Just a Dummy Function which returns None
    N1 : fist Argument
    N2 : Second Argument
    """
    return None

# print(MyFunction.__doc__)

#### Built in Doc Strings

# print(list.__doc__)
# print(set.__doc__)
# print(dict.__doc__)

def  todoList(*Args):
    """
    todoList(*Args) --> Function that receives variable no of Arguments & Returns None.
    """
    print(Args)

def Role(**Kwargs):
    """
    todoList(*Args) --> Function that receives variable no of Keyword Arguments & Returns None.
    Name - Name of the Person
    Role - Expertise of the Person
    Organisation - Oraganisation where the person works
    """
    print(Kwargs)

# todoList("Ramesh","Software Engineer","Google")
# print(todoList.__doc__)
Role(Name="Ramesh",Role="Senior Software Engineer",Orgn="Google")
# print(Role.__doc__)

from string import Template

def Engineering(Name,Organisation,Role="SDE III"):
    tempe = Template("${name} is an Brilliant ${role} at ${orgn}")
    S=tempe.substitute(name=Name,orgn=Organisation,role=Role)
    print(S)
    

# Engineering("Ramesh","Google","'Senior Software Engineer'")

### Keyword Arguments
def Arguments(N1,N2,*N, Log="Yes"):
    """Function to demonstrate the Variable and Keyword Arguments
    
    Note : When calling a function which has both args and Kwargs, K
           Kwargs should be called out with Keyword Name
    Args:
        N1 ([type]): Positional Arg
        N2 ([type]): Positional Arg
        Log (str, optional): [description]. Defaults to "Yes".
    """
    print(N1,N2,Log)
    print(*N)

    
# Arguments(1,2,3,4,Log="No")
# print(Arguments.__doc__)

