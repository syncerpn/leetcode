# O(N2) approach using two pointers to iterate over all triplets
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if target == s:
                    return s
                if abs(target - s) < abs(target - ans):
                    ans = s
                if target > s:
                    j += 1
                else:
                    k -= 1
        return ans