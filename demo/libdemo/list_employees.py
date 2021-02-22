f = open("employees.txt", "rt")
employees = {}
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) != 2:
        continue

    dept = parts[0].strip()
    name = parts[1].strip()

    # Ignore if name is empty or dept is empty
    if len(dept) == 0 or len(name) == 0:
        continue

    if dept in employees:
        employees[dept].add(name)  # add name to existing set
    else:
        employees[dept] = {name}   # Add a set with one entry

f.close()

for dept, names in sorted(employees.items()):
    print(f"{dept:5} {','.join(sorted(names))}")
