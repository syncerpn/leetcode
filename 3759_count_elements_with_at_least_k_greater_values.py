# not so easy
# nice problem
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = Counter(nums)
        nums = sorted(list(set(nums)), reverse=True)
        ans = 0
        for a in nums:
            if ans >= k:
                break
            ans += d[a]
        return n - ans