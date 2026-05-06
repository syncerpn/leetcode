# make it static and shared across test cases would be faster
class Solution:
    def smallestValue(self, n: int) -> int:
        P = [False] * (n + 1)
        S = [0] * (n + 1)
        for a in range(2, n + 1):
            if P[a]:
                continue
            S[a] = a
            b = a
            while b * a <= n:
                m = b * a
                P[m] = True
                b += 1

        for a in range(2, n + 1):
            if P[a]:
                continue
            b = a
            while b * a <= n:
                m = b * a
                S[m] = a + S[b]
                b += 1

        while n != S[n]:
            n = S[n]
        return n