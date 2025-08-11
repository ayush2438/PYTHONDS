class A:
    value="A"

class B(A):
    value="B"

class C(A):
    value="C"

class D(B,C):
    pass

cup=D()
print(cup.value)
print(D.mro())