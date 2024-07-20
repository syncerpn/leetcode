# follow-up #2874 with higher constraints
# it is really just pure array
# we keep track of max result, max difference between ni and nj, and max ni
# the logic is:
# 1. if there any larger ni as we iterate the array
# 1a. if there is any smaller nj, then we got bigger diff and the old diff is no longer needed
# 1b. if there is an nj which is larger than old nj but diff is also larger, we have the new diff tracked
# 1c. if there is an nj which is larger than old nj but diff is smaller, we still have the diff tracked with no update
# whatever the case is, we have enough information about the best one so far
# nk is just a part of the result, so tracking the result has the best of both worlds
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        r = 0
        ni_max = 0
        dij_max = 0
        for n in nums:
            r = max(r, dij_max * n)
            dij_max = max(dij_max, ni_max - n)
            ni_max = max(ni_max, n)
        return r