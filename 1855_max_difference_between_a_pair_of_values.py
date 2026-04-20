# bisect solution
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        ans = 0
        for i, a in enumerate(nums1):
            j = bisect.bisect_right(nums2, -a, key=lambda x: -x)
            if j != 0 and i <= j:
                ans = max(ans, j - 1 - i)
        return ans

# maybe just two-pointer
# it has been a long time i just forgot two-point exist lol
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        j = 0
        n = len(nums2)
        ans = 0
        for i, a in enumerate(nums1):
            while j < n and a <= nums2[j]:
                j += 1
            if j <= n:
                ans = max(ans, j - 1 - i)
        return ans

# a better implementation
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        i = 0
        for j in range(n):
            if nums1[i] > nums2[j]:
                i += 1
                if i >= m:
                    break

        return max(j - i, 0)