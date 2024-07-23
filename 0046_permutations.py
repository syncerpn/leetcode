# recursion solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        result = []
        for i, n in enumerate(nums):
            for p in self.permute([k for j, k in enumerate(nums) if j != i]):
                result.append([n] + p)
        return result

# backtracking solution
# for practicing backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(p):
            if len(p) == len(nums):
                result.append(p)
            else:
                for n in nums:
                    q = p[:]
                    if n not in q:
                        q.append(n)
                        backtrack(q)

        backtrack([])
        return result