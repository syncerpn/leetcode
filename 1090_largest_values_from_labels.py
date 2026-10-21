# greedy
class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        A = [(v, l) for v, l in zip(values, labels)]
        A.sort(reverse=True)
        ans = 0
        d = {}
        for v, l in A:
            if l not in d:
                d[l] = 0
            d[l] += 1
            if d[l] > useLimit:
                continue
            ans += v
            numWanted -= 1
            if numWanted == 0:
                break
        return ans