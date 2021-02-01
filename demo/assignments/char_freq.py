st = "How are you today?"

for ch in sorted(set(st)):
    print(f"{ch} occurs {st.count(ch)} times")