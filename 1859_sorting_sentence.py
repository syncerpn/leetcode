# simply assign word to index
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        s_sorted = [""] * len(s)
        for w in s:
            s_sorted[int(w[-1])-1] = w[:-1]
        
        return " ".join(s_sorted)