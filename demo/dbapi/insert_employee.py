import sqlite3

con = sqlite3.connect(r"d:\classroom\jan18p\hr.db")
cur = con.cursor()
name = input("Enter name :")
job = input("Enter job :")
salary = int(input("Enter salary :"))
try:
    cur.execute("insert into employees(fullname,job,salary) values(?,?,?)", (name, job, salary))
    print("Added Employee Successfully!")
    con.commit()  # Commit Transaction
except Exception as ex:
    print("Error : ", ex)

cur.close()
con.close()
