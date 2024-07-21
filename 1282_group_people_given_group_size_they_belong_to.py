# pretty easy
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        res = []
        for i, g in enumerate(groupSizes):
            if g not in d:
                d[g] = []
            d[g].append(i)
            if len(d[g]) == g:
                res.append(d[g][:])
                d[g] = []
        return res