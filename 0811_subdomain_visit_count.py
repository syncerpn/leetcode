# pure counting and string manip
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for ns in cpdomains:
            n, s = ns.split(" ")
            n = int(n)
            if s not in d:
                d[s] = 0
            d[s] += n

            while (i := s.find(".")) != -1:
                r = s[i+1:]
                if r not in d:
                    d[r] = 0
                d[r] += n
                s = r
        return [str(d[s]) + " " + s for s in d]