# it looks easy
# but it is not
# need to think of various conditions
# the following solution ease our brains, yet obviously not optimal, lol
class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = {}
        for c in word:
            if c not in d:
                d[c] = 0
            d[c] += 1

        v = sorted(d.values())
        return (len(v) == 1) or (v[0] == v[-2] and v[-1] - v[0] == 1) or (v[0] == 1 and v[1] == v[-1])