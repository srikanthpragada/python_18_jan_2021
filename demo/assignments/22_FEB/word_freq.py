# Word freq for words in file

with open(r"d:\classroom\old_man.txt", "rt") as f:
    content = f.read()
    words = content.split(" ")
    for w in sorted(set(words)):
        w = w.strip()
        w = w.replace("\n", '')  # remove \n from string
        print(f"{w:10}  {words.count(w):2}")
