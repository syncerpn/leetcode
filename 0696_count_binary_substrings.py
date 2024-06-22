# count consecutive 0s and 1s
# then pairing them
# we can form substrings from those pair
# where the number of substrings can be formed equal the min of counts of the two
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c = 1
        t = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                c += 1
            else:
                t.append(c)
                c = 1
        
        t.append(c)
        r = 0
        for i, j in pairwise(t):
            r += min(i, j)
        
        return r

