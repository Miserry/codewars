nums = [0]

cnt = 0
mmax = 0

for i in range(len(nums)):
    if nums[i] == 1:
        cnt += 1
        if cnt > mmax:
            mmax += 1
    else:
        cnt = 0
print(mmax)