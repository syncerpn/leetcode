# this is easy
# but somehow the implementation runs slowly
# probably due to list concat
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        d = Counter(sum([list(set(r)) for r in responses], start=[]))
        return min(d, key=lambda k: (-d[k], k))

# this is faster
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        d = Counter()
        for r in responses:
            d.update(set(r))
        m = max(d.values())

        return min(k for k in d if d[k] == m)