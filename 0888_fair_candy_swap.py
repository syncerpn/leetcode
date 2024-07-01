# two-pointer sorting is trivial
# this one use set, reducing time complexity to O(n)
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a = set(aliceSizes)
        b = set(bobSizes)
        d = (sum(aliceSizes) - sum(bobSizes)) // 2
        
        for ai in a:
            if ai - d in b:
                return [ai, ai - d]
        
        return [0, 0]
