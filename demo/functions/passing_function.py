# Passing function as parameter
def mathop(operation, a, b):
    print(operation(a, b))


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


mathop(add, 10, 20)
mathop(multiply, 10, 20)
