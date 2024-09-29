# sort and greedy
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        ans = maximumHeight[0]
        p = maximumHeight[0]
        for h in maximumHeight[1:]:
            h = min(h, p-1)
            if h == 0:
                return -1
            ans += h
            p = h
        return ans