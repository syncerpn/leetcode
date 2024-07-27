# easy
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d, T, F = {}, set(), set()

        for _, t, f in orders:
            t = int(t)
            T.add(t)
            F.add(f)
            if t not in d:
                d[t] = {}
            if f not in d[t]:
                d[t][f] = 0
            d[t][f] += 1

        T, F = sorted(list(T)), sorted(list(F))
        return [["Table"] + F] + [[str(t)] + ["0" if f not in d[t] else str(d[t][f]) for f in F] for t in T]