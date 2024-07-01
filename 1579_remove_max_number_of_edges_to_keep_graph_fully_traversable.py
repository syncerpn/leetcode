# pretty good problem
# this one is my solution
# proud i solved it myself, so i include it here
# ALSO check out union-find
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # we define a function that likely creates/updates a network "sectors"
        # each sector in sectors is a set of nodes that one can traversal internally, with provided edges
        # with an edge (p, q) connect to a node in a sector, then p, q should be grouped into that sector
        def update_sectors(sectors, p, q):
            k = None
            j = 0
            need_new_sector = True
            while j < len(sectors):
                if p in sectors[j] or q in sectors[j]:
                    if k is None:
                        k = j
                        # we add the nodes to the sector
                        sectors[j].add(p)
                        sectors[j].add(q)
                        j += 1
                    else:
                        # this is the case where two sectors are bridged by the edge
                        # so we join them into a single sector
                        sectors[k].update(sectors[j])
                        del sectors[j]
                    need_new_sector = False # if there is no sector containing p or q, we create a new sector
                else:
                    j += 1
            
            if need_new_sector:
                sectors.append(set([p,q]))
        
        # we always need at least n-1 edge to make a sector out of n nodes
        if len(edges) < n-1:
            return -1
        
        # we create sectors that alice and bob can traversal, as well as one that both can use
        sectors = []
        sectors_a = []
        sectors_b = []
        
        for i, e in enumerate(edges):
            t, p, q = e
            if t == 1 or t == 3:
                update_sectors(sectors_a, p, q)
            if t == 2 or t == 3:
                update_sectors(sectors_b, p, q)
            if t == 3:
                update_sectors(sectors, p, q)
        
        # in the end, alice and bob must be able to traversal their own single sector
        if len(sectors_a) != 1 or len(sectors_b) != 1:
            return -1
        
        # and that single sector must have n nodes
        if len(sectors_a[0]) < n or len(sectors_b[0]) < n:
            return -1
        
        min_sectors_edges = 0
        c = 0
        for s in sectors:
            min_sectors_edges += len(s) - 1
            c += len(s)
        
        # for each sector in common sectors, an n-node sector needs at least n-1 edges to ensure traversable
        # we then treat each sector in common sectors as one node, combined with nodes that is not in common sectors
        # if there is k in total, we need at least k-1 edges to ensure traversable
        # double the amount for alice and bob
        return len(edges) - min_sectors_edges - (n-c+len(sectors)-1) * 2
        