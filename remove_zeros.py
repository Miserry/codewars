"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""


nums = [0,1,0,3,12]

for i in range(len(nums)):
    if nums[i] == 0:
        nums.append(nums.pop(i))