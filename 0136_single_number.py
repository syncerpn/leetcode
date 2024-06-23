# using XOR
# XOR a pair of the same number results in 0
# so if we XOR everything, the result will be equals to the single number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for n in nums:
            x = x ^ n
        
        return x