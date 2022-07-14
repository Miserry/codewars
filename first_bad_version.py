# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        #binary, in order to minimize the API calls.

        left = 0
        right = n - 1
        while left <= right:
            mid = int(left + (right - left) / 2)    #searching for the middle point
            if isBadVersion(mid):                   #True if mid is bad version
                right = mid - 1
            else:                                   #if mid is not bad version, any version before that should be good
                left = mid + 1
        return left
