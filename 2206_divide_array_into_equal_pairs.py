# count of each element should be even
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1

        for n in d:
            if d[n] % 2 == 1:
                return False
        
        return True