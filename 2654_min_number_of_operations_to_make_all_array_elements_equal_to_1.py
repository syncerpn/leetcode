# O(n2) solution
# tried to have an O(n) solution without success
# the idea can be summarized by
# trying to the shortest subarray with gcd of all elements be 1
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones, n = 0, len(nums)
        for a in nums:
            if a == 1:
                ones += 1
        if ones > 0:
            return n - ones

        ans = -1
        for i, a in enumerate(nums):
            for j in range(i+1, n):
                a = math.gcd(a, nums[j])
                if a == 1:
                    d = n + j - i - 1
                    if ans == -1:
                        ans = d
                    else:
                        ans = min(ans, d)
                    break
        
        return ans
