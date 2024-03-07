from threading import Thread
from collections import namedtuple

Ramesh=namedtuple("Ramesh",["Role", "Orgn", "Skill"])

R = Ramesh("SDE-3","Google", "Software Development")
R_M = Ramesh("Sr SDE", "Microsoft", "Software Engineering")

print(R[0])  #Acces Item using Index
print(R.Skill) #Access Item using Key Name
print(R_M[1])
print(R_M[2])
print(getattr(R,"Orgn")) #Access Item using getAttr

# print(namedtuple.__doc__)


# di = {"Role": "SRE", "Orgn": "Walmart", "Skill": 'DevOps Expert'}
# print(Ramesh(**di))
# print(R._fields)
