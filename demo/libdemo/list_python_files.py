import os

stdir = r"d:\classroom\jan18p"

allfiles = os.walk(stdir)

for (name, dirs, files) in allfiles:
    if name.find('.git') >= 0:
        continue

    for f in files:
        if f.endswith(".py"):
            print(name + "\\" + f)
