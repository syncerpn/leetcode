# try concat and test after len of concated == len of s
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        r = ""
        for word in words:
            r += word
            if len(r) == len(s):
                return r == s
            elif len(r) > len(s):
                return False
        
        return r == s