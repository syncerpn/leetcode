# more backtrack practice
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(r, i, j):
            if i == j:
                r.append([])
            else:
                backtrack(r, i+1, j)
                ri = []
                for p in result:
                    ri.append([nums[i]] + p)
                r += ri

        backtrack(result, 0, len(nums))
        return result