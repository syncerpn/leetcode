# this is similar to topological sort (or it is topological sort)
# we keep track of node degree (i.e. number of nodes follows each node)
# and child nodes
# then do bfs to update ancestors of each node
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = [set() for _ in range(n)] # child nodes
        r = [0 for _ in range(n)] # node degree
        for f, t in edges:
            d[f].add(t)
            r[t] += 1
        
        # we start from 0-degree nodes and keep going next
        root = [i for i in range(n) if r[i] == 0]
        
        a = [set() for _ in range(n)]
        while root:
            root_next = set()
            for f in root:
                for t in d[f]:
                    # update ancestor and ancestors of ancestor to each node
                    a[t].add(f)
                    a[t].update(a[f])
                    r[t] -= 1

                    # if its degree is now 0, we will start from it next time
                    if r[t] == 0:
                        root_next.add(t)
            
            root = root_next
                
        return [sorted(list(ai)) for ai in a]
