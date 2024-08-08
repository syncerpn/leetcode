# how about a hash table/counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        ans = []
        def backtrack(d, p):
            if len(p) == len(nums):
                ans.append(p[:])
            else:
                for i in d:
                    if d[i] > 0:
                        p.append(i)
                        d[i] -= 1

                        backtrack(d, p)
                        
                        p.pop()
                        d[i] += 1
        
        backtrack(d, [])
        return ans