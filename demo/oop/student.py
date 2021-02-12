class Student:
    # class attributes or static variables
    taxrate = 12
    courses = {'python': 5000, 'java': 6000}

    @staticmethod
    def add_course(name, fee):
        Student.courses[name] = fee

    def __init__(self, admno, name, course='python'):
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = 0

    def payment(self, amount):
        self.feepaid += amount

    def print_details(self):
        print(self.admno, self.name, self.course, self.feepaid)

    def total_fee(self):
        fee = Student.courses[self.course]
        tax = fee * Student.taxrate / 100
        return fee + tax

    def due(self):
        return self.total_fee() - self.feepaid


Student.add_course('ds', 10000)

s1 = Student(1, "Scott")
s1.payment(3000)
s1.print_details()
print(s1.due())
s2 = Student(2, "Mike", "ds")
print(s2.due())
