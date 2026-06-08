# dp
# but need revisit
class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i, a in enumerate(nums):
            p[i+1] = p[i] + a
        
        dp_prev = [0] * (n + 1)
        ans = -inf
        for t in range(1, m + 1):
            dp = [-inf] * (n + 1)
            q = deque()
            for i in range(1, n + 1):
                j = i - l
                if j >= 0:
                    v = dp_prev[j] - p[j]
                    while q and q[-1][1] < v:
                        q.pop()
                    q.append((j, v))
                
                j = i - r
                while q and q[0][0] < j:
                    q.popleft()
                
                dp[i] = dp[i - 1]
                if q:
                    dp[i] = max(dp[i], p[i] + q[0][1])
            
            ans = max(ans, dp[n])
            dp_prev = dp

        return ans