# optimized backtracking
# dont overthinking it
# just distribute
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        v = [0] * k
        ans = [sum(cookies)]
        def solve(l):
            if l == n:
                maxm = 0
                for i in range(k):
                    maxm = max(maxm, v[i])
                ans[0] = min(ans[0], maxm)
            else:
                for i in range(k):
                    v[i] += cookies[l]
                    solve(l+1)
                    v[i] -= cookies[l]
                    if v[i] == 0:
                        break
        
        solve(0)
        return ans[0]