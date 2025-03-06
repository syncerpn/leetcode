# sort and count
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c < i+1:
                return i
        
        return n