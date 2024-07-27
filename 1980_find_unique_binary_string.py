# use set and binary conversion
# trivial solution
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set([sum([int(c) << (n-1-i) for i, c in enumerate(s)]) for s in nums])
        print(nums)
        for i in range(1 << n):
            if i not in nums:
                b = [str((i >> (n-1-j)) & 1) for j in range(n)]
                return "".join(b)
        return ""

# OMG solution
# where we set the bit-i of the result to opposite of bit-i of nums[i]
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = list(nums[0])
        for i, n in enumerate(nums):
            s[i] = "1" if n[i] == "0" else "0"
        return "".join(s)

# maybe we could guess randomly a number within the range and check
# this one has very high success rate as n increases