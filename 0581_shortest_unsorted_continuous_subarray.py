# O(n) with go-go logic
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = -1, n - 1
        
        p = -inf
        for i in range(n):
            if nums[i] < p:
                l = i
                break
            p = nums[i]
        else:
            return 0

        p = inf
        for i in range(n-1, l-1, -1):
            if nums[i] > p:
                r = i
                break
            p = nums[i]
        else:
            r = l

        mi, ma = inf, -inf
        for i in range(l, r + 1):
            mi = min(mi, nums[i])
            ma = max(ma, nums[i])
        
        while True:
            if l > 0 and mi < nums[l-1]:
                mi = min(mi, nums[l-1])
                ma = max(ma, nums[l-1])
                l -= 1
            elif r < n - 1 and ma > nums[r+1]:
                mi = min(mi, nums[r+1])
                ma = max(ma, nums[r+1])
                r += 1
            else:
                break

        return r - l + 1

# turned into a beautiful implementation
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = -1, -2
        mi, ma = nums[-1], nums[0]
        for i in range(n):
            ma = max(ma, nums[i])
            mi = min(mi, nums[~i])
            if nums[i] < ma:
                r = i
            if nums[~i] > mi:
                l = n - 1 - i
        return r - l + 

# or just sort it, traded for time complexity
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        ans = n
        for i in range(n):
            if nums[i] != s[i]:
                break
            ans -= 1
        l = n-ans
        for i in range(n-1, l, -1):
            if nums[i] != s[i]:
                break
            ans -= 1
        return ans
