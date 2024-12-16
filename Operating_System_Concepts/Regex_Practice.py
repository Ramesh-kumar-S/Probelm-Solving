import re

String = "Ramesh has secured a package of 34 LPA"

pattern = r'\d{2}'
match = re.search(pattern, String)
if match:
    print(f"Found {match.group()}")
    
pattern = r'\w\w \w\w\w:\w\w\w'
string = "Ramesh is an MTS:SDE"
if match := re.search(pattern, string):
    print(f'Match Found : {match.group()}')

pattern = r'\s'
print(re.split(pattern, string))


match = re.search(r' \w\w\wured\sa\spackage\s\w\w\s\d\dLPA', String)
if match:
    print(f'Hey {match.group()}')

email = "xyz alice-b@google.com purple monkey"
match1 = re.search(r'[\w.-]+@[\w.-]+', email)
match = re.search(r'\w+\s[a-zA-Z-]+@[a-zA-Z-]+\.[a-z]{3}', email)
if match:
    print(match.group(), match1.group())
    print(type(match.group()))




class TypeHint(object):
    def __init__(self, data : list, new_data : list[dict]) -> None:
        pass

def SoftwareEngineer(role):
    def Role(function):
        def Name(*args, **kwargs):
            return function(role, Name = kwargs["Name"])
        return Name
    return Role

@SoftwareEngineer("MTS-III")
def SDE(Role=None ,Name=None):
    return f'{Name} is an {Role} at NetApp.'

print(SDE(Name="Ramesh"))
    