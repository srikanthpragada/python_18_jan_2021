f = open("names.txt", "rt")
for name in sorted(set(f.readlines())):
    print(name, end='')

f.close()
