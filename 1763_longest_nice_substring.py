# this solution came to my mind naturally
# then i realized it is divide and conquer
# so i think it is a great example of divide and conquer
# nice problem btw
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 0:
            return ""

        # we will find all the "not nice" chars and store them in a set
        nice = set()
        charset = set()
        for c in s:
            if c in nice:
                continue
            charset.add(c)
            if c.upper() != c and c.upper() in charset:
                nice.add(c)
                nice.add(c.upper())
            elif c.lower() != c and c.lower() in charset:
                nice.add(c)
                nice.add(c.lower())
        
        # is there is no "not nice", then probably the whole string is nice
        if charset == nice:
            return s
        
        # otherwise
        j = 0
        r = ""
        s += "#"
        for i, c in enumerate(s):
            # we break s into substrings that do not contain any "not nice" char
            if c not in nice:
                ri = self.longestNiceSubstring(s[j:i])
                # and take the longest one as the final result
                if len(ri) > len(r):
                    r = ri
                j = i+1
        
        return r