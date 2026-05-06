# backtracking
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        v = [0]
        ans = []
        def backtrack(n, k):
            if n == 0:
                ans.append(v[0])
                return
            d = v[0] % 10 - k
            if d >= 0:
                v[0] = v[0] * 10 + d
                backtrack(n-1, k)
                v[0] //= 10
            d = v[0] % 10 + k
            if k > 0 and d <= 9:
                v[0] = v[0] * 10 + d
                backtrack(n-1, k)
                v[0] //= 10
        
        for i in range(1, 10):
            v[0] = i
            backtrack(n-1, k)
        return ans