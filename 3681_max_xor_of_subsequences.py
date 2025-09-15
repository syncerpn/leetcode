# try to remember this because it is a basic problem in algorithm
# we need to build a: linear xor basis set
# the answer will be xor of all numbers in the set
# to build that, we build the basis for each bit position
# geeksforgeeks sample code
class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        nums = list(set(nums))
        k, n = 0, len(nums)
        for i in range(31, -1, -1):
            m = -1
            for j in range(k, n):
                if (nums[j] >> i) & 1:
                    if m == -1 or nums[j] > nums[m]:
                        m = j
            if m == -1:
                continue
            nums[k], nums[m] = nums[m], nums[k]
            for j in range(n):
                if j != k and (nums[j] >> i) & 1:
                    nums[j] ^= nums[k]
            k += 1
        ans = 0
        for a in nums:
            ans ^= a
        return ans

# another way to make a basis set
class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis = []
        for x in nums:
            for b in basis:
                x = min(x, x^b)
            if x > 0:
                basis.append(x)
                basis.sort(reverse=True)
        
        ans = 0
        for b in basis:
            ans = max(ans, ans ^ b)

        return ans

# more way, but a bit slow
class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis = [0] * 32
        for a in nums:
            while a != 0:
                for i in range(31, -1, -1):
                    if a >> i & 1:
                        if basis[i] == 0:
                            basis[i] = a
                        else:
                            a ^= basis[i]
                        break
        ans = 0
        for b in basis[::-1]:
            ans = max(ans, ans ^ b)
        return ans