import sqlite3

con = sqlite3.connect(r"d:\classroom\jan18p\hr.db")
cur = con.cursor()
cur.execute("select * from employees order by id")
for id, name, job, salary in cur.fetchall():
    print(f"{id:3} {name:30} {job:10} {salary:10}")

con.close()
