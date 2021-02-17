
try:
    v = int(input("Enter a number :"))
    print(100 / v)
except ValueError as ex:
    print("Invalid number!", ex)
finally:
    print("Finally block")

print("The End!")
