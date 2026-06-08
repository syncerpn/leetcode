# sliding window
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = None
        q = deque()
        for i, c in enumerate(s):
            if c != "1":
                continue
            q.append(i)
            while len(q) > k:
                q.popleft()
            if len(q) == k:
                t = s[q[0]:q[-1]+1]
                if not ans or len(ans) > len(t):
                    ans = t
                elif len(ans) == len(t):
                    ans = min(ans, t)
        return ans if ans else ""