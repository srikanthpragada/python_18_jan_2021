class A:
    def process(self):
        print("Process of A")


class B(A):
    pass


class C:
    def process(self):
        print("Process of C")


class D(B, C):
    pass


obj = D()
obj.process()
