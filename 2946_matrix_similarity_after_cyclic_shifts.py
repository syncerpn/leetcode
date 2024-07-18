# may not be optimal, but clean
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k = k % len(mat[0])
        return [p[k:] + p[:k] if i % 2 == 0 else p[-k:] + p[:-k] for i, p in enumerate(mat)] == mat