# this is a bit overcomplicated, trying to walk through each diagonal
# simpler solution may just be comparing one with its next diagonal with for w in for h loop
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        h, w = len(matrix), len(matrix[0])
        for wi in range(w):
            ref_value = matrix[0][wi]
            hi = 1
            while hi+wi < w and hi < h:
                if matrix[hi][hi+wi] != ref_value:
                    return False
                hi += 1
        for hi in range(1, h):
            ref_value = matrix[hi][0]
            wi = 1
            while hi+wi < h and wi < w:
                if matrix[hi+wi][wi] != ref_value:
                    return False
                wi += 1
        
        return True