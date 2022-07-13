#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
#The relative order of the elements should be kept the same.

#Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.

#Return k after placing the final result in the first k slots of nums.




nums = [0,0,1,1,1,2,2,3,3,4]

k = 0

for num in nums[1:]:
    if num == nums[k]:
        nums += [nums.pop(k)]   #I didn't know that we can pop a random index position,
    else:                       #but adding the popped index value to the end of the list makes absolute sense in our case.
        k += 1

print(k+1, nums)

#Have to admit that i have struggled quite a bit solving this without using another list to store the values.