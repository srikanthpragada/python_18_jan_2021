# Display average of positive numbers
total = 0
count = 0
while True:
    num = int(input("Enter number [0 to stop]:"))
    if num == 0:
        break   # Terminate loop

    if num < 0:
        continue

    total += num
    count += 1

if count > 0:
    print(f"Average  = {total//count}")
else:
    print("Sorry! No positive number given!")

