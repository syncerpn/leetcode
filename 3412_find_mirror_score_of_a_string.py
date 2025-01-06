# really, easier than the easy question
class Solution:
    def calculateScore(self, s: str) -> int:
        A, Z = "abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"
        AZ = {a: z for a, z in zip(A, Z)}
        d = {c: [] for c in A}
        ans = 0
        for i, c in enumerate(s):
            if d[AZ[c]]:
                ans += i - d[AZ[c]].pop()
            else:
                d[c].append(i)
        return ans