# good problem for practicing this kind of three-partition hashing pattern
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        d = {}
        r = 0
        for i in range(1, len(nums)-1):
            if nums[i-1] not in d:
                d[nums[i-1]] = 0
            d[nums[i-1]] += 1
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    continue
                a, b = 0, 0
                if nums[i] in d:
                    a = d[nums[i]]
                if nums[j] in d:
                    b = d[nums[j]]
                r += i - a - b
        
        return r

# some went crazy with this O(n) single pass solution
# it is just awesome to learn
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        d = {}
        triplets, pairs = 0, 0
        # so we will count number of distinct pairs and triplets on the way
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = 0
            # new triplets can be formed from pairs removing those containing n
            triplets += pairs - d[n] * (i - d[n])
            # new pairs can be formed from element passed so far removing count of n
            pairs += i - d[n]
            d[n] += 1
        return triplets
