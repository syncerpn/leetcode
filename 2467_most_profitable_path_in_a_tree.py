# very nice problem
# it looks hard at the first glance, but then you realize that the graph is a tree
# so there should be only one path for bob to move towards 0
# and then, it just becomes super easy to find the reward for alice
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        g = {}
        for a, b in edges:
            if a not in g:
                g[a] = set()
            g[a].add(b)
            if b not in g:
                g[b] = set()
            g[b].add(a)
        
        pb = {}
        def move(a):
            pb[a] = len(pb)
            if a == 0:
                return True
            for b in g[a]:
                if b not in pb:
                    if move(b):
                        return True
            del pb[a]
            return False
        
        move(bob)

        pa = {}
        ans = [-float("inf")]
        def move_reward(a, r):
            pa[a] = len(pa)
            if a not in pb or pa[a] < pb[a]:
                r += amount[a]
            elif pa[a] == pb[a]:
                r += amount[a] // 2
            if a != 0 and len(g[a]) == 1:
                ans[0] = max(ans[0], r)
            else:
                for b in g[a]:
                    if b not in pa:
                        move_reward(b, r)
            del pa[a]
        
        move_reward(0, 0)
        return ans[0]