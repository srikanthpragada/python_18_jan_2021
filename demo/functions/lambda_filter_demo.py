
nums = [10, 11, 19, 80, 66, 75]
for n in filter(lambda v: v % 2 == 0, nums):
    print(n)

for n in filter(lambda v: v % 2 != 0, nums):
    print(n)