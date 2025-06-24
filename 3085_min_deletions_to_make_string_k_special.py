# greedy counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = Counter(word)
        ans = len(word)
        for a in d:
            t = 0
            for b in d:
                if d[b] - d[a] > k:
                    t += d[b] - d[a] - k
                elif d[a] > d[b]:
                    t += d[b]
            ans = min(ans, t)
        return ans