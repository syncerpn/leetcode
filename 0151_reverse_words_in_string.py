# python makes it easy
class Solution:
    def reverseWords(self, s: str) -> str:
        r = [si for si in s.split(" ") if si != ""]
        return " ".join(r[::-1])