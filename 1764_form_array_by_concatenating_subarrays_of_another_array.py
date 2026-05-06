# brute-force search
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        for grp in groups: 
            for ii in range(i, len(nums)):
                if nums[ii:ii+len(grp)] == grp: 
                    i = ii + len(grp)
                    break 
            else: return False
        return True

# or better with kmp
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        for group in groups:
            g = len(group)
            failure = [0] * g
            j = 0
            for k in range(1, g):
                while j > 0 and group[j] != group[k]:
                    j = failure[j-1]
                j += group[j] == group[k]
                failure[k] = j
            j = 0
            for k in range(i, n):
                while j > 0 and group[j] != nums[k]:
                    j = failure[j-1]
                j += group[j] == nums[k]
                if j == g:
                    i = k + 1
                    break
            else:
                return False
        return True