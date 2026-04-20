# easy
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            d = Counter(nums)
            return len([a for a in d if d[a] > 1])

        K = set(nums)
        nums = sorted(list(K))
        ans = 0
        for a in nums:
            if (a + k) in K:
                ans += 1
        return ans