# two cases based on odd or even length
# odd length is easy because peaks fall into every odd-indexed element
# with even length, we need to break the array into two odd-length parts
# that should also minimize the increment ops
# this can be done with precomputed forward and backward peaks
class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        if n % 2 == 0:
            l, r = 0, 0
            L, R = [0], [0]
            for i in range(1, n-1, 2):
                l += max(0, max(nums[i-1], nums[i+1]) + 1 - nums[i])
                L.append(l)
            for i in range(-2, -n, -2):
                r += max(0, max(nums[i-1], nums[i+1]) + 1 - nums[i])
                R.append(r)
            return min(L[i] + R[~i] for i in range(len(L)))
        
        ans = 0
        for i in range(1, n, 2):
            ans += max(0, max(nums[i-1], nums[i+1]) + 1 - nums[i])
        return ans

# nice dp solution
# would you skip or take i as a peak
class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        take, skip = 0, 0
        if n % 2:
            for i in range(1, n, 2):
                take += max(0, max(nums[i-1], nums[i+1]) + 1 - nums[i  ])
        else:
            for i in range(2, n-1, 2):
                take += max(0, max(nums[i-1], nums[i+1]) + 1 - nums[i  ])
                skip += max(0, max(nums[i-2], nums[i  ]) + 1 - nums[i-1])
                if skip < take:
                    take = skip
        return take