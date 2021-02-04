# Keyword only arguments
def area(*, width, length):
    return length * width


print(area(length=10, width=20))
print(area(width=20, length=50))
