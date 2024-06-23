# became one-liner for this one, lol
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([si[::-1] for si in s.split(" ")])