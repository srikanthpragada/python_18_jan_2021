def numbers():
    for n in range(1, 6):
        yield n


nums = numbers()
print(type(nums))
print(next(nums))
