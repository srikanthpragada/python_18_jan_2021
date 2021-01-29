
st = "This is to test"

chars = []
for c in st:
    if c not in chars:
        chars.append(c)


print(chars)