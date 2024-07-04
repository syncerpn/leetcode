# sort with custom key
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        indices = list(range(len(mat)))
        indices.sort(key=lambda i: sum(mat[i]))
        return indices[:k]