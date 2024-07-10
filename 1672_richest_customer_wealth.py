# fair straight forward
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(m) for m in accounts])