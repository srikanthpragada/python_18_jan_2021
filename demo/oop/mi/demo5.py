class A:
    def process(self):
        print("Process in A")


class B:
    def process(self):
        print("Process in B")


class C(A, B):
    def process(self):
        A.process(self)
        B.process(self)


obj = C()
obj.process()
