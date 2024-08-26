# hash table solution
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        ans = 0
        for i in d:
            if d[i] == 0:
                continue
            
            j = k - i
            if i == j:
                ans += d[i] // 2
            elif j in d and d[j] > 0:
                m = min(d[j], d[i])
                ans += m
                d[j] -= m
                d[i] -= m
        return ans

# sorting + two pointer
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = 0
        while i < j < len(nums):
            if nums[i] + nums[j] == k:
                i += 1
                j -= 1
                ans += 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
        return ans

# hash table but single pass
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        ans = 0
        for n in nums:
            if k-n in d and d[k-n] > 0:
                ans += 1
                d[k-n] -= 1
            else:
                if n not in d:
                    d[n] = 0
                d[n] += 1
        return ans
                