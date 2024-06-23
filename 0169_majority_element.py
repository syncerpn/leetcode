# use dict, O(N) time and space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        m = nums[0]
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
            if d[m] < d[n]:
                m = n
        
        return m

# use Moore voting algorithm, O(N) time and O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 1
        m = nums[0]

        for n in nums[1:]:
            if c == 0:
                m = n
                c = 1
            elif m == n:
                c += 1
            else:
                c -= 1
        
        return m