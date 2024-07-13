# super nice "easy" problem, lol
# O(n4) is bruteforce
# O(n3) with a single dict was me
# O(n2) is just beautiful
# its like we divide the array into two,
# trying to form two two-sum parts
# and update the dict as it goes,
# instead of preparing everything at the start
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ab, res = {}, 0
        for b in range(1, len(nums)-2):
            # taking b as the second num index
            # going backward to count the sum of nums[a] + nums[b]
            # this step updates the dict with exhaustive nums[a] + nums[b] found
            for a in range(b):
                if nums[a]+nums[b] not in ab:
                    ab[nums[a]+nums[b]] = 0
                ab[nums[a]+nums[b]] += 1
            # meanwhile, taking b+1 as third num index
            # going forward to count the sum of nums[c] + nums[b]
            # this step looks up the dict with exhaustive nums[d] - nums[c]
            # such that its result can be found in the dict of nums[a] + nums[b]
            # if found, then probably nums[a] + nums[b] = nums[d] - nums[c]
            # this sum, nums[a] + nums[b], can be formed by different pairs
            # of nums[a] and nums[b]
            # so we add the count of all results acknowledged in ab dict
            for d in range(b+2, len(nums)):
                if nums[d]-nums[b+1] in ab:
                    res += ab[nums[d]-nums[b+1]]
        return res