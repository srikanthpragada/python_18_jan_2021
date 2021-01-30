data = "90,10,45,98,7,88,abc,34"
nums = []
for m in data.split(","):
    if m.isdigit():
       nums.append(int(m))

for n in sorted(nums):
    print(n)
