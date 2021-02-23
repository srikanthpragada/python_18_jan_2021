# Word freq for words in file

import re

with open(r"d:\classroom\old_man.txt", "rt") as f:
    content = f.read()
    words = re.findall(r"[A-Za-z0-9'_]+",content)
    for w in sorted(set(words)):
        print(f"{w:10}  {words.count(w):2}")
