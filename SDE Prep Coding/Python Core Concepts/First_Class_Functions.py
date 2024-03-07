#Functions as Objects
def Role(role):
    return f'Ramesh is an brilliant {role}'

Job=Role
print(Job("Algorithmic Thinker"))

#######################################################################
#Functions as Arguments
#######################################################################
def square(L):
    return [n*n for n in L]

def Exponential(L):
    return [pow(2,n) for n in L]

def ComplexityAnalysis(func):
    Res=func([3,5,6,7,8,10])
    
    print(Res)

ComplexityAnalysis(square)
ComplexityAnalysis(Exponential)

#######################################################################
# Functions can return another function 
#######################################################################
def create_adder(x): 
    def adder(y): 
        return x+y 
  
    return adder 
  
add_15 = create_adder(15) 
  
print (add_15(10)) 

#######################################################################
# Referencing a Function to an Variable
#######################################################################
LANG="CPP"

def Expertise(name):
    return f'Ramesh is an Brilliant {name}'

def Excellent(name):
    return f'Ramesh is an Excellent {name}'

Role=Expertise if LANG == "PYTHON" else Excellent

print(Role)
print(Role("Algorithmic Thinker"))