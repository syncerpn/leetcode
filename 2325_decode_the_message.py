# remap with map, of course
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        d = {}
        for k in key:
            if k == " ":
                continue
            if k not in d:
                d[k] = ALPHABETS[i]
                i += 1
        
        r = ""
        for c in message:
            if c in d:
                r += d[c]
            else:
                r += c
        
        return r