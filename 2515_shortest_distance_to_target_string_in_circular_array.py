# going both directions at the same speed
# stop right when one found
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        if words[startIndex] == target:
            return 0
        
        i = (startIndex + 1) % n
        j = (startIndex - 1) % n
        c = 1
        while i != startIndex:
            if words[i] == target:
                return c
            if words[j] == target:
                return c
            c += 1

            i = (i + 1) % n
            j = (j - 1) % n
        
        return -1