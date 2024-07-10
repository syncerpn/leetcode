# just use set
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        r = len(words)
        for word in words:
            for c in word:
                if c not in allowed:
                    r -= 1
                    break
        return r