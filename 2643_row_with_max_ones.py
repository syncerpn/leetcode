# make it compact
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        c = [[sum(r), -i] for i, r in enumerate(mat)]
        s, ri = max(c)
        return [-ri, s]