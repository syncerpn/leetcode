# we can perform one op for multiple value a if there is no value smaller than a in between them
# for example: [2, 3, 2] is possible to convert two 2 into 0 in one op
# but [2, 1, 2] is not possible
# so we have to track an mono-increasing array
# to find out if the current value can be merge with a previous one if any
# un-mergable value will be popped from the array and requires one op to convert to zero
# also be aware of 0 already value
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        ans = 0
        for a in nums:
            while s and s[-1] > a:
                ans += 1
                s.pop()
            if not s or s[-1] != a:
                s.append(a)
        return ans + len(s) - (s[0] == 0)