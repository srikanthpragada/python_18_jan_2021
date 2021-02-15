class A:
    def process(self):
        print("Process of A")


class B:
    def process(self):
        print("Process of B")


class C(A, B):
    pass


obj = C()
obj.process()
