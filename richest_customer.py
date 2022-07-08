class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        acc = []
        for i in accounts:
            acc.append(sum(i))
        big_acc = max(acc)
        return big_acc
