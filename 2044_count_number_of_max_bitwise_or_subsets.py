# this is similar to max subset sum, but use bitwise or instead
# solved with dp
# we need to the following things in order
# 0. init an empty hash table/counter for counting
# 1. iterate the array
# 2. we will try to add the current num n to any subset already in counter so far
# the counter will count the subset bitwise or result
# so its keys are bitwise or results of the subset
# and its values are number of setsubs with such results
# 3. as we or n with each k in counter, we create a new subnet
# 4. add the count of such subset bitwise or result into counter
# 5. add count of n into d at the last step before the next iteration
# this is n acting as a subset itself (i.e. subset with a single element n)
# to avoid error due to hash table size changes during count update in step 2-4
# also, as we update the count, we dont use the new count until the next iteration
# to avoid duplicated counting which leads to a wrong result
# (see comment in the code)
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        d = {}
        m = 0
        for n in nums:
            m |= n
            kc = list(d.items())
            for k, c in kc:
                p = k | n
                if p not in d:
                    d[p] = 0
                # we must use c, instead of d[k] to avoid duplicated counting
                d[p] += c
            if n not in d:
                d[n] = 0
            d[n] += 1
        return d[m]