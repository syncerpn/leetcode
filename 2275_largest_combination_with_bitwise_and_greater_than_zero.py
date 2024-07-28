class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        b = [0] * 32
        for n in candidates:
            for i in range(32):
                b[i] += (n >> i) & 1
        
        return max(b)