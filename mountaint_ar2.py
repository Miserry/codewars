#validMountainArray = [1, 2, 3, 4, 5, 2, 1]
#invalid = [1, 2, 3, 3, 5, 3, 1]

#Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]




def validMountainArray(arr: list[int]) -> bool:

    high = arr.index(max(arr))

    # for i in arr:                      #i was searching for the mountain high in a very slow way.
    #     if i == max(arr):
    #         break
    #     else:
    #         high += 1

    if arr[0] >= arr[high] or arr[-1] >= arr[high]:
        return False

    for j in range(1, high):
        if arr[j - 1] >= arr[j]:
            return False

    for k in range(high + 1, len(arr)):
        if arr[k] >= arr[k - 1]:
            return False

    return True

print(validMountainArray([1,1,1,1,1,1,1,2,1]))

