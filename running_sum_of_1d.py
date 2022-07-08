class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bash_lst = []
        lst = []
        for i in nums:
            lst.append(i)
            bash_lst.append(sum(lst))
        return bash_lst
