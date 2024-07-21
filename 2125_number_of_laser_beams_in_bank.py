# built-in count("1") is much faster than manual counting
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        r = 0
        d = 0
        for b in bank:
            s = b.count("1")
            if s > 0:
                r += d * s
                d = s
        return r