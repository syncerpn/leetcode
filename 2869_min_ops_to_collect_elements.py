# use set
# either like below
# or you can create set of range k and eventuall remove elements from it
# until reaching empty set
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = 0
        s = set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] <= k and nums[i] not in s:
                s.add(nums[i])
                c += 1
            if c == k:
                return len(nums)-i
        return -1
