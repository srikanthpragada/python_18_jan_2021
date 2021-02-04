# Positional only arguments
def area(length, width, /):
    return length * width


print(area(10, 20))
# print(area(length = 10, width = 20))
