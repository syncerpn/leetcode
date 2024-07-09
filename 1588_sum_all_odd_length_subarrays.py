# marked as easy, but the solution is not easy lol
# the O(n) solution is here
# given any element in arr
# any subarray containing the element should start at an index smaller or equal to i
# and end at an index bigger or equal to i
# we can count the number of starting indices and ending indices
# then the number of subarray is any pair of starting and ending indices
# because we count only odd-length subarray
# that should be bigger half of them
# which is ceil(num_subarray_contains_ai / 2)
# or here with int: num_subarray_contains_ai - num_subarray_contains_ai // 2
# it is just beautiful
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        r = 0
        for i, a in enumerate(arr):
            num_subarray_contains_ai = (i+1) * (n-i)
            r += a * (num_subarray_contains_ai - num_subarray_contains_ai // 2)
        return r