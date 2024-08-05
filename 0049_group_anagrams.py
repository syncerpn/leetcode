# sort and count
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in d:
                d[ss] = []
            d[ss].append(s)
        return [d[ss] for ss in d]