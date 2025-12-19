# first try: sort meeting time and try to connect people
# -> but during connecting, there is no guarantee we start connecting from a good person, so we may ignore pair of bad persons; order matters
# second try: merge meeting time, sort the order so that we can start from good person first
# -> yet still cannot guarantee the order of pairs of bad persons
# final try: so we need graph update with cached update
# -> when somebody is updated, propagate the update to ones connected to that person; also implementation matters to get a nice runtime
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        md = {}
        for a, b, t in meetings:
            if t not in md:
                md[t] = []
            md[t].append([a, b])
        
        T = sorted(list(md.keys()))
        d = [False] * n
        d[0] = True
        d[firstPerson] = True
        for t in T:
            g = {}
            s = []
            for a, b in md[t]:
                if d[a] and d[b]:
                    continue
                elif d[a] and not d[b]:
                    d[b] = True
                    s.append(b)
                elif d[b] and not d[a]:
                    d[a] = True
                    s.append(a)
                else:
                    if a not in g:
                        g[a] = []
                    g[a].append(b)
                    if b not in g:
                        g[b] = []
                    g[b].append(a)
            while s:
                a = s.pop()
                if a in g:
                    for b in g[a]:
                        if not d[b]:
                            d[b] = True
                            s.append(b)

        return [i for i, b in enumerate(d) if b]