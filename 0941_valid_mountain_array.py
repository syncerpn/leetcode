# mountain should have both inc and dec slopes, so length should be at least 3
# any two consecutive points of same value causes false
# once reached turning point, it should never go up again
# again, in the end, dec slope must exist
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        inc = None
        for p, n in pairwise(arr):
            if p == n:
                return False
            if inc is None:
                if n < p:
                    return False
                inc = True
            elif not inc and n > p:
                return False
            elif inc and n < p:
                inc = False
        
        return not inc