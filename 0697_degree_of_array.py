# here we track count, first index, and on-going last index
# by that, we can measure subarray length as well as freq
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        d_min = len(nums)
        c_max = 0
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = [1, i, i]
            else:
                d[n] = [d[n][0] + 1, d[n][1], i]
            
            if d[n][0] > c_max:
                d_min = d[n][2] - d[n][1] + 1
                c_max = d[n][0]
            elif d[n][0] == c_max:
                if d[n][2] - d[n][1] + 1 < d_min:
                    d_min = d[n][2] - d[n][1] + 1
        
        return d_min