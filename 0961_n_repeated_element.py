# hashmap is trivial
# this one uses random
# because half of the numbers are the same, we have 50% * 50% = 25% chance of picking the same number twice
# and we use O(1) space
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 1
        while nums[i] != nums[j] or i == j:
            i = random.randint(0, n-1)
            j = random.randint(0, n-1)
        return nums[i]