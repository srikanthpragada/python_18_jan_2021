# Take a number from user and print table

num = int(input("Enter a number :"))
i = 1
while i <= 10:
    print(f"{num:3} * {i:2} = {num*i:5}")
    i += 1