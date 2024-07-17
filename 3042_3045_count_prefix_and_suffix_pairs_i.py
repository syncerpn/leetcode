# this is ok for brute-force
# try the follow-up in #3045, which is much harder
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                a = words[i]
                b = words[j]
                if len(a) > len(b):
                    continue
                if b[:len(a)] == a and b[-len(a):] == a:
                    c += 1
        return c