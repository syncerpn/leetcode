# count with hash table
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
            if d[n] > 2:
                return False
        return True