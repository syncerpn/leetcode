# need to enforce some conditions into target and between nums and target
# pretty nice prob
class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        n = len(nums)
        p = -inf
        d = {}
        cand = []
        for i in range(n-1, -1, -1):
            if target[i] < p:
                break
            a, b = nums[i], target[i]
            if a not in d:
                d[a] = 0
            d[a] += 1
            if d[a] == 0:
                del d[a]
            if b not in d:
                d[b] = 0
            d[b] -= 1
            if d[b] == 0:
                del d[b]
            if not d:
                cand.append(-i)
            p = target[i]

        l = n - 1
        for i in range(n):
            if nums[i] != target[i]:
                l = i
                break
        return len(cand) - bisect.bisect_left(cand, -l)