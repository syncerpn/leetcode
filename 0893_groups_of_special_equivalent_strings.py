# divide strings into odd and even parts, then sort and add to set
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        s = set()
        for w in words:
            we = sorted(w[::2])
            wo = sorted(w[1::2])
            s.add("".join(we + wo))
        return len(s)