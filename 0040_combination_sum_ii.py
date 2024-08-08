# there is a trick to skip duplicates
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(s, v, l):
            if s == target:
                ans.append(v[:])
            elif s < target:
                for i in range(l, len(candidates)):
                    # skip possible duplicates
                    if i > l and candidates[i] == candidates[i-1]:
                        continue
                    s += candidates[i]
                    v.append(candidates[i])

                    backtrack(s, v, i+1)

                    s -= candidates[i]
                    v.pop()
        
        candidates.sort()
        backtrack(0, [], 0)
        return ans