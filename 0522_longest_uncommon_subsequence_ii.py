# greedy check for subsequence; have not found any better way yet
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(x, y):
            it = iter(y)
            return all(c in it for c in x)

        strs = sorted(strs, key=lambda s: -len(s))
        for i, s in enumerate(strs):
            j = 0
            while j < i:
                if is_subseq(s, strs[j]):
                    break
                j += 1
            else:
                j += 1
                while j < len(strs) and len(strs[j]) == len(s):
                    if is_subseq(s, strs[j]):
                        break
                    j += 1
                else:
                    return len(s)
        
        return -1