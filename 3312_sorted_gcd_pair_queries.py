# need revisit
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        
        mx = max(nums)
        freq = [0] * (mx + 1)
        for a in nums: 
            freq[a] += 1
            
        GCD = [0] * (mx + 1)
        
        for i in range(mx, 0, -1):
            sm = sum(freq[i::i])
            GCD[i] = sm * (sm - 1) // 2 - sum(GCD[i::i])
            
        GCD = list(accumulate(GCD))
        
        return [bisect.bisect_right(GCD, q) for q in queries]