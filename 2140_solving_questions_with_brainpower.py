# my logic with heapq
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        h = []
        heapq.heapify(h)
        m = 0
        for i, (p, b) in enumerate(questions):
            while h:
                j, k = heapq.heappop(h)
                if j >= i:
                    heapq.heappush(h, (j, k))
                    break
                m = max(m, k)
            heapq.heappush(h, (b+i, m+p))
        
        while h:
            j, k = heapq.heappop(h)
            m = max(m, k)
        return m

# solving with dp should be the better way
# from end to beginning, the best point:
# whether you take it d[i]
# or you dont take it m[i]
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        d = [0] * n
        m = [0] * n
        d[-1] = questions[-1][0]
        for i in range(n-2, -1, -1):
            p, b = questions[i]
            m[i] = max(d[i+1], m[i+1])
            d[i] = p + (max(m[i+b+1], d[i+b+1]) if i+b+1 < n else 0)
        
        return max(m[0], d[0])

# but this is better
# previously, why needs so much info, such as m??
# try this
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            p, b = questions[i]
            dp[i] = max(dp[i+1], p + (dp[i+b+1] if i+b+1 <= n else 0))
        return dp[0]