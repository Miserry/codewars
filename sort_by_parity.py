nums = [3,1,2,4]

for i in range(len(nums)):
    count = i
    while nums[i] % 2 != 0:
        nums.append(nums.pop(i))
        count += 1
        if count >= len(nums):
            break
print(nums)