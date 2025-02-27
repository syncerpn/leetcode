# kind of brute force like
# properly can be further optimized
# need to revisit
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