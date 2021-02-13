class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def category(self):
        if self.age < 40:
            return "Young"
        elif self.age < 60:
            return "Middle-Aged"
        else:
            return "Old"

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        # print('__gt__')
        return self.age > other.age


p1 = Person("Scott", 44)
print(p1.category)   # Property
p2 = Person("Anders", 45)
p3 = Person("Scott", 34)

# print(p1)  # str(p1)  -> p1.__str__()
# print(p1 == p3)  # p1.__eq__(p3)
# print(p1 != p3)  # p1.__eq__(p3)
# print(p2 > p1)
#
# persons = [Person('A', 30), Person('C', 50), Person('B', 20)]
#
# for p in sorted(persons):
#     print(p)
