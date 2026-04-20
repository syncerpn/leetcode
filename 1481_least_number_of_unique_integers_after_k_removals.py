# easy
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = Counter(arr)
        s = [(d[k], k) for k in d]
        s.sort()
        n = len(s)
        ans = n
        i = 0
        while k > 0 and i < n:
            k -= s[i][0]
            i += 1
            if k >= 0:
                ans -= 1
        return ans
        