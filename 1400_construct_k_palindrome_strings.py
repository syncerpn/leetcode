# count every chars in s
# it is only valid if len(s) >= k and the amount of odd chars <= k
# expanded
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = 0
        d = {}
        for c in s:
            if c not in d:
                d[c] = False
            d[c] = not d[c]
            n += 1
        return n >= k and sum(d[c] for c in d if d[c]) <= k

# or faster with lib
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k and sum(v%2 for _, v in Counter(s).items()) <= k