# first thought
# actually we just need the shortest >= k length
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        P = []
        n = len(s)
        def find_palindrome(i):
            l, r = i, i+1
            d = 2
            while l >= 0 and r <= n - 1:
                if s[l] != s[r]:
                    l += 1
                    r -= 1
                    d -= 2
                    if d >= k:
                        P.append((r, l))
                    break
                elif d >= k:
                    P.append((r, l))
                    break
                l -= 1
                r += 1
                d += 2
            
            l, r = i, i
            d = 1
            while l >= 0 and r <= n - 1:
                if s[l] != s[r]:
                    l += 1
                    r -= 1
                    d -= 2
                    if d >= k:
                        P.append((r, l))
                    break
                elif d >= k:
                    P.append((r, l))
                    break
                l -= 1
                r += 1
                d += 2

        for i in range(n):
            find_palindrome(i)
        P.sort()
        dp = [0] * (n + 1)
        for r, l in P:
            for i in range(-1, l):
                dp[r] = max(dp[r], dp[i] + 1)
        return max(dp)

# actually just use sliding window for O(kn)
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        n = len(s)
        ans = 0
        start = 0
        for r in range(k - 1, n):
            l = r - k + 1

            if l >= start and check(l, r):
                ans += 1
                start = r + 1
                continue
            
            l = r - k
            if l >= start and check(l, r):
                ans += 1
                start = r + 1

        return ans