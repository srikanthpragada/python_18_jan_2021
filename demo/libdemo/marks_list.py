f = open("marks.txt", "rt")
students = {}

for line in f.readlines():
    if len(line.strip()) == 0: # if line is blank, ignore
        continue

    values = line.split(",")
    name = values[0]
    marks = [int(v) for v in values[1:] if v.isdigit()]
    avg_marks = sum(marks) / len(marks)
    students[name] = (sum(marks), avg_marks)

f.close()

for name, (total, avg) in sorted(students.items()):
    print(f"{name:20} {total:6} {avg:6.2f}")
