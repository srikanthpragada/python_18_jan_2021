def iseven(n: int) -> bool:
    return n % 2 == 0


def hasdigit(st: str) -> bool:
    for c in st:
        if c.isdigit():
            return True

    return False


nums = [10, 11, 19, 80, 66, 75]
for n in filter(iseven, nums):
    print(n)

for c in filter(str.isupper, 'Hi Greek'):
    print(c)

names = ['Abc', "Xyz1", 'Pqr2', 'Def', '9Bbc']

for n in filter(hasdigit, names):
    print(n)


for n in names:
    if  hasdigit(n):
        print(n)

