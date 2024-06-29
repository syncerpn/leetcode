class Solution:
    def toLowerCase(self, s: str) -> str:
        r = ""
        for c in s:
            r += c.lower()
        return r