# hash map
# possible because of low constraints
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def get_all_substrings(s):
            n = len(s)
            return Counter([s[i:j+1] for i in range(n) for j in range(i, n)])
        d = Counter()
        for s in arr:
            d += get_all_substrings(s)
        
        ans = []
        for s in arr:
            p = get_all_substrings(s)
            d -= p
            for pi in sorted(p.keys(), key=lambda x: (len(x), x)):
                if d[pi] == 0:
                    ans.append(pi)
                    break
            else:
                ans.append("")
            d += p
        return ans