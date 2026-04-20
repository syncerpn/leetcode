# easy
class Solution:
    def longestWord(self, words: List[str]) -> str:
        d = set(words)
        ans = ""
        for word in sorted(words):
            s = ""
            for c in word[:-1]:
                s += c
                if s not in d:
                    break
            else:
                if len(word) > len(ans):
                    ans = word
        return ans