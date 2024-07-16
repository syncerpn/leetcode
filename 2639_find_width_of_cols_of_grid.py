# zip unpack into cols
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max([len(str(c)) for c in p]) for p in zip(*grid)]