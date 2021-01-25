
num = int(input("Enter a number :"))

prime = True
for n in range(2, num//2 + 1):
    if num % n == 0:
        prime = False
        break

if prime:
    print("Prime number!")
else:
    print("Not a Prime number!")

