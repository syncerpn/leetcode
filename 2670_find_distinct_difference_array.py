# hash table, and set
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        d = {}
        for k in nums:
            if k not in d:
                d[k] = 0
            d[k] += 1

        s = len(d.keys())
        n = len(nums)
        diff = [0] * n
        l = set()
        for i in range(n):
            k = nums[i]
            l.add(k)
            d[k] -= 1
            if d[k] == 0:
                s -= 1
            diff[i] = len(l) - s
        return diff