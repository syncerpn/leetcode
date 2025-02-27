# kind of brute force like, O(n2logn)
# logn because fibo seq grows fast enough to be just logn
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        d = set(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                p = arr[i]
                q = arr[j]
                k = 2
                while p + q in d:
                    p, q = q, p + q
                    print(q)
                    k += 1
                if k > 2:
                    ans = max(ans, k)
        return ans

# dp O(n2)
# dp[a, b] is length of the fibo seq ends up with (a, b)
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = {}
        s = set(arr)
        for j in range(len(arr)):
            for i in range(j):
                ai, aj = arr[i], arr[j]
                if aj - ai < ai and aj - ai in s:
                    dp[ai, aj] = dp.get((aj - ai, ai), 2) + 1
        return max(dp.values() or [0])