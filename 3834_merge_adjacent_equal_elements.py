# easy stack
class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        s = []
        for a in nums:
            while s and s[-1] == a:
                a += s.pop()
            s.append(a)
        return s