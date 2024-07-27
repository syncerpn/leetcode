# make it as graph
# try to find the first and last elements, each of which has only one adjacent
# rebuild the array starting from these two elements
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = {}
        v = set()
        for a, b in adjacentPairs:
            if a not in d:
                d[a] = []
            d[a].append(b)
            if b not in d:
                d[b] = []
            d[b].append(a)
            if a not in v:
                v.add(a)
            else:
                v.discard(a)
            if b not in v:
                v.add(b)
            else:
                v.discard(b)

        v = list(v)
        ans, last = [v[0]], v[1]
        p = None
        while ans[-1] != last:
            for k in d[ans[-1]]:
                if k != p:
                    ans.append(k)
            p = ans[-2]

        return ans