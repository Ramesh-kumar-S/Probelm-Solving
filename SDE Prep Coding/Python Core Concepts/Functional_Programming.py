from functools import reduce
from functools import partial

#Find out the Average version of a storage controllers using List comprehension
Controllers = [{
        "Name" : "Rio Beach",
        "Type" : "RAID",
        "Version" : 8.6
    },{
        "Name" : "Knox",
        "Type" : "Tri Mode RAID",
        "Version" : 9.2
    },
    {
        "Name" : "Noe Valley",
        "Type" : "M.2 SATA",
        "Version" : 7.9
    }]

# print(len(Controllers))

#Use Map Function to add a vendor to a List of controllers
def append_Vendor(x):
    x['Vendor'] = "Cisco"
    return x
print("\n --------  Appending Vendor to the Controller----------------\n")
print(list(map(append_Vendor,Controllers)))

#Use Filer Function to Return a version that > 8
def version_Greaterthan8(x):
    return x['Version'] >= 8
print("\n --------  Controllers Version Greater than 8 ----------------\n")
print(list(filter(version_Greaterthan8,Controllers)))

#Use Reduce to get the Average Version of the controller
Versions = [int(controller['Version']) for controller in Controllers]
def average_Version(accumValue,CurValue):
    return accumValue + CurValue
print("\n --------  Average Controllers Version - Reduced ----------------\n")
print(reduce(average_Version, Versions)//len(Controllers))

Result = [controller['Version'] for controller in Controllers]
print("\n --------  Average Controllers Version ----------------\n")
print(sum(Result)//len(Controllers))


print("\n --------  Partial Function via Built in Method ----------------\n")
def Engineer(x,y,z):
    return f'{x} is an Brilliant & Diplomatic {y} at {z} Ever.'

SDE=partial(Engineer,y="Software Engineer",z="Microsoft")
print(SDE("Ramesh Kumar Sekar"))

print("\n --------  Partial Function via Closure and Currying Method----------------\n")
def curry_Name(x):
    def curry_Role(y):
        def curry_Organisation(z):
            return f'{x} is an Brilliant & Buisness oriented {y} at {z} Ever.'
        return curry_Organisation
    return curry_Role

Name = curry_Name("Ramesh")
Role = Name("Computer Scientist")
Organisation = Role("Google")
print(Organisation)
# SoftwareEngineer("Ramesh","Computer Scientist","Google")
