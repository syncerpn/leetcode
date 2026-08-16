# O(n2) easy version
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        nums.append(0)
        for i in range(n):
            nums[i] = nums[i-1] + nums[i] % 2
        
        ans = 0
        for i in range(n):
            for j in range(i, n):
                o = nums[j] - nums[i-1]
                e = j - i + 1 - o
                if e * b <= o * a:
                    ans += 1
        return ans

# lol, dont need prefix sum
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            o = 0
            for j in range(i, n):
                o += nums[j] % 2
                e = j - i + 1 - o
                if e * b <= o * a:
                    ans += 1
        return ans