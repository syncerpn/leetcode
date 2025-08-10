# this is wrong solution, accepted due to weak test-cases
# check all numbers that are not in the correct positions
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        k = n
        for i, a in enumerate(nums):
            if i == a:
                continue
            k = min(k, i & a)

        return 0 if k == n else k

# accumulate bitwise-and is the right way
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        for i, a in enumerate(nums):
            if i == a:
                continue
            k &= a

        return 0 if k == -1 else k

# proof of work should lie in the fact that
# all misplaced numbers must be swapped
# so k must be a accum bitwise-and result of all the misplaced
# and that k & x <= k for any x
# so there cant be any other large value of k