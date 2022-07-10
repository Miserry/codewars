nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3

nums = nums1[:m]+nums2[:n]
nums.sort()
lst = []
for num in nums:
    lst.append(num)
lst.sort()
for i in range(n+m):
    nums1[i] = lst[i]

print(nums1)
