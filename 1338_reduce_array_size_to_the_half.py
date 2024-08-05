# counter and greedy selection
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        t, s = 0, 0
        for k in sorted(Counter(arr).values(), reverse=True):
            t += k
            s += 1
            if t >= n // 2:
                break
        return s