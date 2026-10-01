# easy
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        d = {}
        A = []
        for a in nums:
            if a not in d:
                d[a] = 0
                A.append(a)
            d[a] += 1
        A.sort()
        s = []
        for a in A:
            for i in range(d[a]):
                if i >= len(s):
                    s.append([a])
                else:
                    s[i].append(a)
        ans = []
        for si in s:
            ans += si
        return ans