# Display tasks in the sorted order of start date
from datetime import datetime

f = open("tasks.txt", "rt")
tasks = []
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:  # not enough data
        continue
        
    try:
        stdate = datetime.strptime(parts[1].strip(), "%d-%m-%Y")
    except:
        continue

    if len(parts) == 2:  # no enddate
        enddate = datetime.today()
    else:
        try:
            enddate = datetime.strptime(parts[2].strip(), "%d-%m-%Y")
        except:
            continue

    t = (parts[0], stdate, enddate, (enddate - stdate).days)
    tasks.append(t)

# Sort tasks by start date
for task in sorted(tasks, key=lambda t: t[1]):
    print(f"{task[0]:50} {task[1].strftime('%d-%m-%Y'):12} {task[3]:3}")
