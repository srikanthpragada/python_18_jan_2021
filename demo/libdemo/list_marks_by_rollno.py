# Read information from marks.xml
# and print rollno and marks in the sorted order of rollno

from bs4 import BeautifulSoup

f = open("marks.xml", "rt")
bs = BeautifulSoup(f.read(), "lxml-xml")
f.close()

students = bs.find_all("student")
student_marks = {}
for student in students:
    rollno = student.find("rollno").text
    marks = student.find("marks").text
    student_marks[rollno] = marks

for rollno, marks in sorted(student_marks.items()):
    print(f"{rollno:5} {marks}")
