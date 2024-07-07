# check all source cities
# then any dest city not in source city set should be the answer
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for si, _ in paths:
            s.add(si)
        for _, di in paths:
            if di not in s:
                return di