# make a tree
# then memoi + traverse
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        tree = {i: [] for i in range(len(edges) + 1)}
        size = {}
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        s = [0]
        while s:
            s_next = []
            for a in s:
                for b in tree[a]:
                    if a in tree[b]:
                        tree[b].remove(a)
                    s_next.append(b)
            s = s_next

        def tree_size(r):
            if r not in size:
                p = 1
                for s in tree[r]:
                    if s not in size:
                        size[s] = tree_size(s)
                    p += size[s]
                
                size[r] = p
            return size[r]
        
        ans = 0
        for a in tree:
            b_size = [tree_size(b) for b in tree[a]]
            if len(set(b_size)) <= 1:
                ans += 1
        return ans