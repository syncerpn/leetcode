# fairly simple
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        c = []
        for i, n in enumerate(nums):
            if n == x:
                c.append(i)
        
        return [c[q-1] if q <= len(c) else -1 for q in queries]