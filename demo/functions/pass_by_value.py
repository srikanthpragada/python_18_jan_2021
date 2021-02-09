def zero(v):
    v = 0


def prepend(lst, value):
    lst.insert(0, value)


a = 100
zero(a)
print(a)

# Passing mutable object
l = [1,2,3]
prepend(l,100)
print(l)
