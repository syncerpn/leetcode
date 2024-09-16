# begin getting used to dp
# feel much more confident
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, ms = len(s), set(len(w) for w in wordDict)
        wordDict = set(wordDict)
        v = set([0])
        while v and n not in v:
            v_n = set()
            for i in v:
                for m in ms:
                    if i+m <= n and s[i:i+m] in wordDict:
                        v_n.add(i+m)
            v = v_n
        return n in v