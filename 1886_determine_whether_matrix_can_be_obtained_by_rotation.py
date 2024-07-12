# try rotate and compare
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            n = len(mat)
            mat = [r[::-1] for r in mat]
            mat = [[*p] for p in zip(*mat)]
            return mat
        
        if mat == target:
            return True
        for _ in range(3):
            mat = rotate(mat)
            if mat == target:
                return True
        return False