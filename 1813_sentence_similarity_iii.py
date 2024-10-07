# the low acceptance really scared me at first
# but it turned out pretty easy
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        if len(s1) > len(s2):
            return self.areSentencesSimilar(sentence2, sentence1)
        
        m, n = len(s1), len(s2)
        i = 0
        while i < m and s1[i] == s2[i]:
            i += 1
        
        j = -1
        while m + j >= i and s1[j] == s2[j]:
            j -= 1
        return i == m + j + 1