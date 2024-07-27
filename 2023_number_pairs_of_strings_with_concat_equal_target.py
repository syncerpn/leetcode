# counting one-pass O(nm)
# gradually add count during iteration
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        d = {}
        ans = 0
        for n in nums:
            if target.startswith(n):
                k = target[len(n):]
                if k in d:
                    ans += d[k]
            if target.endswith(n):
                k = target[:-len(n)]
                if k in d:
                    ans += d[k]

            if n not in d:
                d[n] = 0
            d[n] += 1
        return ans