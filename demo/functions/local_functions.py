a = 1  # Global variable


def fun1():
    global a
    a = a + 1
    b = 10  # Enclosing variable
    print("In fun1()", a, b)

    def fun2():  # Local function
        nonlocal b
        b = 1000
        c = 100  # Local Variable
        print("In fun2()", a, b, c)

    fun2()
    print(b)


fun1()
print(a)
