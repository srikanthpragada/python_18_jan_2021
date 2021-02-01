st = "How are you today How you were yesterday"

words = st.split(" ")

# Take unique words from list
for w in set(words):
    print(f"{w} occurs {words.count(w)} times")