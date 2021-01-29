data = "90,10,45,98,7,88,34"
nums = []
for m in data.split(","):
    nums.append(int(m))

for n in sorted(nums):
    print(n)
