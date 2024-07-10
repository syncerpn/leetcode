class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        nums.sort(key=lambda a: (d[a], -a))
        return nums