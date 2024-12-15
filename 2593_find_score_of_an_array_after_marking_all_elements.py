# sort and mark
class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans = 0
        k = len(nums)
        d = [False] * k
        c = 0
        s = sorted([(n, i) for i, n in enumerate(nums)])
        for n, i in s:
            if d[i]:
                continue
            ans += n
            d[i] = True
            c += 1
            if i > 0:
                c += d[i-1]
                d[i-1] = True
            if i < k - 1:
                c += d[i+1]
                d[i+1] = True
            if c == k:
                break
        return ans