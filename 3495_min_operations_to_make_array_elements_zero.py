# no need anything complex like seg tree
# just do it as power of 4 linear check
# if a >= 4 ** i, it will need i + 1 operations to reduce it to 0
# and for a query, just count how many operations to make all the numbers to 0
# then divide it by 2, taking ceil, because in one actual operation, we can reduce at most 2 numbers by one level
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def range_sum(l, r):
            d, s = 1, 0
            while d <= r:
                s += r - max(l, d) + 1
                d <<= 2
            return (s + 1) >> 1
        return sum(range_sum(*q) for q in queries)