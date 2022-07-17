#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
#The relative order of the elements should be kept the same.

#Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.

#Return k after placing the final result in the first k slots of nums.

def removeDuplicates(nums: List[int]) -> int:
    """
    k = 1
    Start a for (i) loop to mark the current number, 
        if i no in nums[:k], k += 1
        else, nums.append(nums.pop(k))
    """
    k = 1
    for i in nums[1:]:
        if i not in nums[:k]:
            k += 1
        else:
            nums.append(nums.pop(k))
    return k

