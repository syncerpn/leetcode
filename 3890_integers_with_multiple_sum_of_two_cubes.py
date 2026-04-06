# easy
class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        D = []
        a = 0
        while (aaa := a ** 3) < n:
            D.append(aaa)
            a += 1
        k = len(D)
        v = set()
        ans = []
        for a in range(1, k):
            for b in range(a, k):
                s = D[a] + D[b]
                if s > n:
                    break
                if s not in v:
                    v.add(s)
                else:
                    ans.append(s)
        return sorted(list(set(ans)))