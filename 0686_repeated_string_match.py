# there are only two cases if matching is possible
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        t = math.ceil(len(b) / len(a))
        if b in a * t:
            return t
        if b in a * (t + 1):
            return t + 1
        return -1

# actual implementation for checking if b is a substring is more complicated
# better learn KMP, z-function, and robin-karp (rolling hash)