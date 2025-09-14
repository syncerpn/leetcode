# easy but not very intuitive
# especially when it comes with a confusing description
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        VOWELS = set(list("aeiou"))
        d = {}
        f = {}
        p = {}
        for s in wordlist:
            sl = s.lower()
            if sl not in d:
                d[sl] = set()
                f[sl] = s
                qi = ""

            for c in sl:
                if c in VOWELS:
                    qi += "*"
                else:
                    qi += c
            if qi not in p:
                p[qi] = s

            d[sl].add(s)
        ans = []
        for q in queries:
            ql = q.lower()
            if ql in d:
                if q in d[ql]:
                    ans.append(q)
                else:
                    ans.append(f[ql])
            else:
                qi = ""
                for c in ql:
                    if c in VOWELS:
                        qi += "*"
                    else:
                        qi += c
                if qi in p:
                    ans.append(p[qi])
                else:
                    ans.append("")
        return ans