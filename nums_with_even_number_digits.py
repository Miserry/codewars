nums = [13,16,253,35422,34545,65464765,65433]
count = 0
#print(len(str(nums[1])))
for i in nums:
    if len(str(i)) % 2 == 0:
        count += 1

print(count)