# easy
class Solution:
    def reverseWords(self, s: str) -> str:
        V = set(list("aeiou"))
        s = s.split(" ")
        d = sum(c in V for c in s[0])
        return " ".join([s[0]] + [si[::-1] if sum(c in V for c in si) == d else si for si in s[1:]])