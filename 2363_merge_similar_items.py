# easy problem that mentions orderedset
# because it is easy, can be solved with custom implementation of list and dict
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        from sortedcontainers import SortedDict
        d = SortedDict()
        for v, w in items1:
            d[v] = w
        
        for v, w in items2:
            if v not in d:
                d[v] = w
            else:
                d[v] += w
        
        return [[v, d[v]] for v in d]
