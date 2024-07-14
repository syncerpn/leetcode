# similar to #2062
# trying to mark two milestone in the array
# start: the starting index of a k-diff-int subarray up to current index
# start_minimal: starting index of the shortest k-diff-int subarray up to current index
# each time we encounter a number that already seen in the k-diff-int set,
# we can form start_minimal - start + 1 more subarrays satisfying the requirements
# otherwise, we need to recheck for start and start_minimal
# because a new not-seen number makes it k+1-diff-int set
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        v = {}
        ki, start, start_minimal = 0, 0, 0
        r = 0
        for i, n in enumerate(nums):
            if n not in v:
                v[n] = 0
            v[n] += 1
            
            ki += v[n] == 1
            
            # recheck for start and start_minimal
            # to ensure a k-diff-int set
            while ki > k:
                v[nums[start_minimal]] -= 1
                if v[nums[start_minimal]] == 0:
                    ki -= 1
                start_minimal += 1
                start = start_minimal
            
            # recheck for start_minimal with the new start found in the prev step
            while v[nums[start_minimal]] > 1:
                v[nums[start_minimal]] -= 1
                start_minimal += 1
            
            # add the count of new subarray formable up to current index i
            if ki == k:
                r += start_minimal - start + 1
        return r