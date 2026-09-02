# backward dp
# f[i] = max score difference from i onward
# so at first, alice take all, thus f[n-1] = pre[n-1]
# at n-2, either alice take up to n-2 and bob take n-1: score diff = pre[n-2] - f[n-1]
# or alice take all: score diff = f[n-1]
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        pre = list(accumulate(stones))
        f = [0] * n
        f[n - 1] = pre[n - 1]
        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], pre[i] - f[i + 1])
        return f[1]
        