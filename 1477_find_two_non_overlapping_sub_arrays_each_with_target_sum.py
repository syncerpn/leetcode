# sliding window
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        m = inf
        d = {0:-1}
        s = deque()
        ans = inf
        p = 0
        for i, a in enumerate(arr):
            p += a
            b = p - target
            if b in d:
                j = d[b]
                l = i - j
                while s and s[0][0] <= j:
                    m = min(m, s[0][1])
                    s.popleft()
                if not s or l < s[-1][1]:
                    s.append((i, l))
                ans = min(ans, l + m)
            d[p] = i
        return ans if ans < inf else -1