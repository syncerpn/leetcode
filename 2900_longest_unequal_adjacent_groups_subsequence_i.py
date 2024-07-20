# seems easy
# how about the follow-up?
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        s = [words[0]]
        p = groups[0]
        for w, g in zip(words[1:], groups[1:]):
            if g != p:
                s.append(w)
                p = g
        
        return s