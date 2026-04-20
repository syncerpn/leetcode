# easy
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        ans = []
        for i in range(n):
            if i > 0 and nums[i] - nums[i-1] < 2:
                continue
            if i < n - 1 and nums[i+1] - nums[i] < 2:
                continue
            ans.append(nums[i])
        return ans

# O(n) solution is a different view of the problem
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        K = set(nums)
        for a in nums:
            d[a] += 1
            d[a-1] += 1
            d[a+1] += 1
        return [a for a in d if d[a] == 1 and a in K]