# Count no. of uppercase letters

st = input("Enter a string :")
count = 0
for c in st:
    if c.isupper():
        count += 1

print(f"No. of uppercase letters = {count}")