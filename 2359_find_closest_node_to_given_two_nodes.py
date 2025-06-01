# easiest way without early stopping
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        node1, node2 = min(node1, node2), max(node1, node2)
        def traverse(s, d, v):
            d[s] = 0
            while s not in v:
                v.add(s)
                b = edges[s]
                if b == -1:
                    break
                d[b] = min(d[b], d[s] + 1)
                s = b

        n = len(edges)
        d1, d2 = [float("inf")] * n, [float("inf")] * n
        v1, v2 = set(), set()
        traverse(node1, d1, v1)
        traverse(node2, d2, v2)
        
        v = v1 & v2
        if not v:
            return -1
        v = sorted(list(v), key=lambda a: (max(d1[a], d2[a]), a))
        return v[0]

# with early stopping
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        visited1 = set()
        visited2 = set()
        while node1 != -1 or node2 != -1:
            if node1 in visited1:
                node1 = -1
            
            if node2 in visited2:
                node2 = -1

            if node1 != -1:
                visited1.add(node1)
            
            if node2 != -1:
                visited2.add(node2)

            if node1 in visited2 and node2 in visited1:
                return min(node1, node2)
            
            if node1 in visited2:
                return node1
            
            if node2 in visited1:
                return node2
            
            if node1 != -1:
                node1 = edges[node1]

            if node2 != -1:
                node2 = edges[node2]       
                 
        return -1