# Display rollno and total for each student
marks = ['1,90','2,80','1,88','3,77','1,87','2,70','3,56']

students = {}

for m in marks:
    rollno, value  = m.split(",")
    if rollno in students:
        students[rollno] = students[rollno] +  int(value)
    else:
        students[rollno] = int(value)

for rollno,total in sorted(students.items()):
    print(f"{rollno:5} {total:4}")


