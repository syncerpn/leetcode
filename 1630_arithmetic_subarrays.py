# good problem
# sorting is trivial
# but without sorting, we can make it O(n), optimally in 2 passes
# first pass, iterate to get min, max of the subarray and build set of subarray element
# we then check:
# if min == max: (or len set == 1): true
# if 1 < len(set) < len(subarray) : false
# if (max - min) % (ri - li) must be zero; otherwise: false
# we then get d = (max - min) // (ri - li)
# this d is expected to be gap of each pair of consecutive elements if sorted
# however, we can still check whether gap of any pair of elements is divisible by d
# if not: false
# this is super useful to remember
# the following implementation uses built-in func instead of actual 2-pass though
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [False] * len(l)
        for i, li, ri in zip(list(range(len(r))), l, r):
            if 1 < len(set(nums[li:ri+1])) < ri - li + 1:
                continue
            a = max(nums[li:ri+1])
            b = min(nums[li:ri+1])
            if a == b:
                ans[i] = True
                continue
            n = ri - li
            if (a - b) % n != 0:
                continue
            d = (a - b) // n
            for x, y in pairwise(nums[li:ri+1]):
                dxy = abs(x - y)
                if dxy % d != 0:
                    break
            else:
                ans[i] = True
            
        return ans