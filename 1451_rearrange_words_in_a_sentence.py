# easy
class Solution:
    def arrangeWords(self, text: str) -> str:
        s = text.split(" ")
        s.sort(key=lambda x: len(x))
        ans = " ".join(s)
        ans = ans[0].upper() + ans[1:].lower()
        return ans