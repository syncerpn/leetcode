# if there are at least two, we can remove one
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))