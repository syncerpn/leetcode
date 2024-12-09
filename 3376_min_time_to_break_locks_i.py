# brute force with permutation
# greedy method did not work and costed me a lot of time debugging
class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        ans = [None]
        def test(p):
            t_total = 0
            X = 1
            for s in p:
                t_total += int(ceil(s / X))
                X += K
                if ans[0] is not None and t_total > ans[0]:
                    break
            if ans[0] is None:
                ans[0] = t_total
            ans[0] = min(ans[0], t_total)

        for p in itertools.permutations(strength):
            test(p)
        
        return ans[0]