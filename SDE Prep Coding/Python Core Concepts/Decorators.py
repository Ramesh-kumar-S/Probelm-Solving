def decor1(func):
    print(func)
    def wrap():
           print("************")
           func()
           print("************")
    return wrap
def decor2(func):
    print(func)
    def wrap():
           print("@@@@@@@@@@@@")
           func()
           print("@@@@@@@@@@@@")
    return wrap
    
@decor1
		
@decor2
def sayhellogfg():
		print("Hello")
def saygfg():
		print("GeekforGeeks")
		
print(sayhellogfg)
print(id(sayhellogfg))
# AA=<function decor1.<locals>.wrap at 0x0000028AF5951CF0>
# AA()
saygfg()


# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
memory = {}
def memoize_factorial(f):
	
	# This inner function has access to memory
	# and 'f'
	def inner(num):
		if num not in memory:
			memory[num] = f(num)
			print('result saved in memory')
		else:
			print('returning result from saved memory')
		return memory[num]

	return inner
	
@memoize_factorial
def facto(num):
	if num == 1:
		return 1
	else:
		return num * facto(num-1)

# print(facto(5))
# print(facto(5)) # directly coming from saved memory




from functools import wraps
from functools import update_wrapper
from functools import  lru_cache

#Class Decorator
class SofwareEngineer:
    def __init__(self,func):
        update_wrapper(self,func)
        self.func=func
        self.role="Computer Scientist"
    
    def __call__(self, *args, **kwargs):
        Res=self.func()
        return  "Ramesh is " + Res + self.role + " in Google"
    
#Function Decorator  
def Ramesh(func):
    @wraps(func)
    def wrapper():
        res="Ramesh - " + func() +"Google."
        return res
    return wrapper

@SofwareEngineer
@lru_cache(maxsize=None )
def SDE():
    """Ramesh's Google PortFolio"""
    return "One of the Finest "
# SDE=SofwareEngineer(SDE)
# print(SDE())

#Chainining the Decorator
def ComputerScientist(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        Res=func(*args,**kwargs) + " is an Finest " + args[0] +" in "
        return  Res
    return wrapper

def Google(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        Res=func(*args,**kwargs) + args[1]
        return  Res
    return wrapper

@Google
@ComputerScientist
# @SoftwareEngineer
def Ramesh(Role,Orgn):
    return "Ramesh"

# print(Ramesh("Computer Scientist","Google"))
# print(Ramesh("Software Engineer","Adobe"))
# print(Ramesh)


