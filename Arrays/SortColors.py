nums = [2,0,2,1,1,0]

count_0 = 0
count_1 = 0
count_2 = 0

for i in nums:
    if i == 0:
        count_0 += 1
    elif i == 1:
        count_1 += 1
    else:
        count_2 += 1
step = 0
for i in range(count_0):
    nums[step] = 0
    step += 1

for i in range(count_1):
    nums[step] = 1
    step += 1

for i in range(count_2):
    nums[step] = 2
    step += 1

print(nums)
        