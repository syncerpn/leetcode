# easy
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        c = 0
        s = 0
        for n in nums:
            if n % 6 == 0:
                c += 1
                s += n
        
        return s // c if c else 0