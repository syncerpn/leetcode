# need to remove empty strings after splitting
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        r = []
        for word in words:
            r += [w for w in word.split(separator) if w]
        return r