
nums = []

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    nums.append(num)

avg = sum(nums) // len(nums)

for n in nums:
    if n >= avg:
        print(n)

