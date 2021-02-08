def odd_even(n):
    return 0 if n % 2 == 0 else 1


nums = [10, 29, 20, 40, 55, 33, 50]
for n in sorted(nums, key=odd_even):
    print(n)
