class A:
    # pass
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    # pass
    def d(self):
        return "Function inside D"


class E(B, C):
    pass
    # def d(self):
    #     return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())

import calendar

print(calendar.month())
