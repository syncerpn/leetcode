# nice problem
# learn/revisit quite a bunch of things
# first, we want to partition the array into multiple parts
# where elements in each part must be swapped internally
# we need to unlock all elements in that part as well
# second, for the sorting part
# it is actually kind of bubble sort swap counter'
# where we will want to iterate and count for each index i, how many index j < i that A[j] > A[i]
# that is when we need a swap to at least make A[j] appears after A[i]
# this can be done in O(nlogn) with fenwick tree or SortedList python (b-tree kind of?)
# so overally it is O(nlogn)
class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        l, r, c = inf, -inf, 0
        swap = 0
        unlock = 0

        for i, a in enumerate(nums):
            r = max(r, a)
            l = min(l, a)
            c += locked[i]
            if r == i + 1:
                if l < r:
                    unlock += c
                    if k < unlock:
                        return -1
                    s = SortedList()
                    p = 0
                    for j in range(l-1, r):
                        b = nums[j]
                        p += len(s) - s.bisect(b)
                        s.add(b)
                    swap += p
                l, r, c = inf, -inf, 0
        return unlock + swap