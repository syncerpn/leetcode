# seems like there is no other better solution than bruteforce
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        s = [len(bin(n))-2 for n in nums]
        ans = [0]
        def dfs(v, t):
            if not v:
                ans[0] = max(ans[0], t)
            else:
                for i in v:
                    t = (t << s[i]) + nums[i]
                    v.discard(i)
                    dfs(v, t)
                    v.add(i)
                    t = (t - nums[i]) >> s[i]
        
        dfs(set([0,1,2]), 0)
        return ans[0]