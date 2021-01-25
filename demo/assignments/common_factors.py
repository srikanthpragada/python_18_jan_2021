
num1 = 9
num2 = 20

small = num1 if num1 < num2 else num2
for n in range(2, small//2 + 1):
    if num1 % n == 0 and num2 % n == 0:
        print(n)


