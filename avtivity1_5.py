#identity operator

x=-9
if(type(x) is int):
    print("true")
else:
    print("false")
x=5.0
if(type(x)is not float):
    print("true")
else:
    print("false")
x=20
y=20
if(x is y):
    print("x and y is the same identity")
y=30
if(x is not y):
    print("x and y have differnt identities")

