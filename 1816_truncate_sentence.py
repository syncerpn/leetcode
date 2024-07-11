# iterate and count number of words passed
# return when we have enough words
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        for i, c in enumerate(s):
            if c == " ":
                k -= 1
                if k == 0:
                    return s[:i]
        
        return s