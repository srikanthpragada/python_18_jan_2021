st = "How do you do?"

pos = -1
while True:
    pos = st.find(' ',pos + 1)
    if pos == -1:
        break
    print(pos)
