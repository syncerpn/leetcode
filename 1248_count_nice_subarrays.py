# this can be solved with prefix sum
# but this solution does differently
# with a bit of math
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # we track positions of odd numbers
        # assuming the pre-first and post-last
        # (not existing in the input) are also odd
        odd_pos = [-1]
        for i, n in enumerate(nums):
            if n % 2:
                odd_pos.append(i)
        odd_pos.append(len(nums))

        n = len(odd_pos)
        c = 0
        for i in range(1, n-k):
            j = i + k - 1
            # for each pair of (i, j) we can take
            # any even number before i and after j
            # to form a cont subarray
            # so the number of subarrays equals product of counts of them
            # count until the two odd numbers
            l = odd_pos[i] - odd_pos[i-1]
            r = odd_pos[j+1] - odd_pos[j]
            c += l * r
        return c