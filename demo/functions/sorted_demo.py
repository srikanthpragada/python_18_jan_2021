nums = [10, -1, 20, -50, 30, -25]

for n in sorted(nums, key=abs):
    print(n)

names = ['java','Ruby','c','JavaScript','Python']
for n in sorted(names, key = len):
    print(n, end = ' ')


