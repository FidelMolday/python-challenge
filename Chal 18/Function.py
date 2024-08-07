#Function
def Additive (item):
    return item + 10

def Substructive (item):
    return item - 10

def Operator(func, x):
    result = func(x)
    return result

print(Operator(Additive, 100))
print(Operator(Substructive, 100))    