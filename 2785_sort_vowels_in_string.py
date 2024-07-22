# no need to sort
# just build it with array
class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = {c: i for i, c in enumerate("AEIOUaeiou")}
        vs = [[] for _ in range(len(VOWELS))]
        s = list(s)
        for c in s:
            if c in VOWELS:
                vs[VOWELS[c]].append(c)
        
        vs = sum(vs, [])
        j = 0
        for i, c in enumerate(s):
            if c in VOWELS:
                s[i] = vs[j]
                j += 1
        return "".join(s)