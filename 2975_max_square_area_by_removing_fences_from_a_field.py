# check all possible sides
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10 ** 9 + 7
        hFences.append(m)
        vFences.append(n)

        ans = -1
        W = set()
        t = 1
        for i in range(len(hFences)):
            for j in range(i, len(hFences)):
                W.add(abs(hFences[j] - t))
            
            t = hFences[i]
            
        t = 1
        for i in range(len(vFences)):
            for j in range(i, len(vFences)):
                h = abs(vFences[j] - t)
                if h in W:
                    ans = max(ans, h * h)
            
            t = vFences[i]
        return -1 if ans == -1 else ans % MOD