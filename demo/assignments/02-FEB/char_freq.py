st = "How are you today?"

chars = {}
for ch in set(st):
    chars[ch] = st.count(ch)

for ch, count in sorted(chars.items()):
    print(ch, count)
