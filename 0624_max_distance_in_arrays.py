# greedy dp is fair
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        d_min = arrays[0][0]
        d_max = arrays[0][-1]
        ans = 0
        for i in range(1, m):
            ans = max(ans, d_max - arrays[i][0], arrays[i][-1] - d_min)
            d_max = max(d_max, arrays[i][-1])
            d_min = min(d_min, arrays[i][0])
        
        return ans