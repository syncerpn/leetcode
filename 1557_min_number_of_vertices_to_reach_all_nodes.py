# use set
# gradually discard all dests
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        s = set(list(range(n)))
        for _, d in edges:
            s.discard(d)
        return s
