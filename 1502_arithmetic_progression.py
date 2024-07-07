# sorting is trivial
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for a, b in pairwise(arr[1:]):
            if b - a != d:
                return False
        return True

# how about an O(n)?
# we will find the gap between two consecutive elements
# make sure that the diff between each element and min of arr is divisible by gap
# and we should have the number of unique diffs equals to length of arr
# pretty nice solution
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a_min = min(arr)
        a_max = max(arr)
        n = len(arr)
        if (a_max - a_min) % (n - 1) != 0:
            return False
        gap = (a_max - a_min) // (n - 1)
        if gap == 0:
            return True
        s = set([a - a_min for a in arr])
        return len(s) == n and all(d % gap == 0 for d in s)